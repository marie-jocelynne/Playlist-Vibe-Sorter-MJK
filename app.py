import gradio as gr

# This is my sample playlist with songs from my favourite artis.
# I used a small list on purpose so the sorting steps are just easier to see.
songs = [
    {"title": "Knot Me", "artist": "Lucy Bedroque", "energy": 55},
    {"title": "butterflies", "artist": "Brent Faiyaz", "energy": 65},
    {"title": "Stateside", "artist": "PinkPantheress & Zara Larsson", "energy": 80},
    {"title": "Risk", "artist": "Deftones", "energy": 90},
    {"title": "Everybody Here Wants You", "artist": "Jeff Buckley", "energy": 50},
    {"title": "Sweet Boy", "artist": "Malcolm Todd", "energy": 60}
]

# I made a global list so I can save each split/merge step
# and show it later in the app output.
steps = []

# This just pulls out song titles so the steps look cleaner.
def get_titles(arr):
    return [song["title"] for song in arr]

# Main Merge Sort function.
# It keeps splitting the list into smaller halves until each part has 1 item,
# then it merges everything back in sorted order.
def merge_sort(arr, key):
    # If the list has 0 or 1 item, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle so the list can be split into 2 halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # I record the split here so the person using it can actually see
    # how Merge Sort breaks the playlist down.
    steps.append(
        f"Split: {get_titles(arr)} -> {get_titles(left_half)} and {get_titles(right_half)}"
    )

    # Recursively sort the left half and the right half.
    left = merge_sort(left_half, key)
    right = merge_sort(right_half, key)

    # Merge the 2 sorted halves back together.
    merged = merge(left, right, key)

    # I record the merged result too so the full process is visible.
    steps.append(f"Merged: {get_titles(merged)}")

    return merged

# This function takes 2 already-sorted halves and combines them
# into 1 sorted list by comparing one item at a time.
def merge(left, right, key):
    result = []
    i = 0
    j = 0

    # Compare songs from both halves using the chosen key.
    # For this project I am sorting by energy.
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If one half still has leftover items, add them at the end.
    # This works because those leftovers are already sorted.
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# This runs the sorting process and formats everything
# so it can be displayed clearly in the Gradio app.
def run_sort():
    global steps
    steps = []

    # Sort the playlist from low energy to high energy.
    sorted_songs = merge_sort(songs, "energy")

    # Build the output text for the app.
    output = "SORTING STEPS:\n\n"
    for step in steps:
        output += step + "\n"

    output += "\nFINAL SORTED PLAYLIST (Low to High Energy):\n\n"
    for song in sorted_songs:
        output += f"{song['title']} by {song['artist']} - Energy: {song['energy']}\n"

    return output

# This creates the simple app interface.
# I kept it basic so it is easy to use.
with gr.Blocks() as demo:
    gr.Markdown("# Playlist Vibe Sorter by Marie-Jocelynne Kasiama")
    gr.Markdown("Click the button to sort the playlist by energy using Merge Sort and see each step.")
    
    output_box = gr.Textbox(label="Sorting Steps + Final Playlist", lines=20)
    
    sort_button = gr.Button("Sort Playlist")
    clear_button = gr.Button("Clear")

    # When clicked, it will run the sorting process and show the steps in the output box
    sort_button.click(fn=run_sort, inputs=None, outputs=output_box)
    clear_button.click(fn=lambda: "", inputs=None, outputs=output_box)

# Launch!!!
demo.launch()
