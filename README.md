# Playlist Vibe Sorter by Marie-Jocelynne Kasiama for CISC 121 (Vizualization) 

## Chosen Problem
I created a playlist sorter that organizes songs based on their energy level. This shows how a sorting algorithm can be used in a real-life situation like music playlists.

## Chosen Algorithm
I used Merge Sort because it is efficient and works by splitting the list into smaller parts, sorting them, and merging them back together. It is also easy to visualize step-by-step.

## Demo

![Demo](demo.gif)

## Problem Breakdown & Computational Thinking

### Decomposition
- Take the playlist
- Split it into smaller lists
- Sort each part
- Merge them back together

### Pattern Recognition
- Repeatedly splitting lists
- Comparing elements
- Merging sorted lists

### Abstraction
- Only show song titles in steps
- Hide extra details to keep it simple

### Algorithm Design
Input → playlist  
Process → merge sort  
Output → sorted playlist + steps  

## Steps to Run
1. Install gradio:
2. Run the app: python3 app.py
3. Open the local URL shown in the terminal (usually http://127.0.0.1:7860)

## Testing

### Test 1 (Normal case)
Expected: playlist sorted by energy  
Actual: songs sorted correctly from lowest to highest energy  

### Test 2 (Already sorted)
Expected: no change  
Actual: output remains the same  

### Test 3 (Small dataset)
Expected: still sorts correctly  
Actual: works properly  

## Hugging Face Link
(Add link here)
