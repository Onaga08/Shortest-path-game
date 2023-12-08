import pygame
import tkinter as tk

def get_adjacency_list(selected_squares):
    adjacency_list = {}

    for square in selected_squares:
        x, y = square
        neighbors = []

        # Check if the squares to the left, right, above, and below are selected
        if (x - 1, y) in selected_squares:
            neighbors.append((x - 1, y))
        if (x + 1, y) in selected_squares:
            neighbors.append((x + 1, y))
        if (x, y - 1) in selected_squares:
            neighbors.append((x, y - 1))
        if (x, y + 1) in selected_squares:
            neighbors.append((x, y + 1))

        adjacency_list[square] = neighbors

    return adjacency_list

def display_adjacency_list(selected_path):
    
    # Get the adjacency list
    adjacency_list = get_adjacency_list(selected_path)

    # Create a tkinter window
    window = tk.Tk()
    window.title("Adjacency List")

    # Create a label to display the adjacency list
    label = tk.Label(window, text="Adjacency List:")
    label.pack()

    for square, neighbors in adjacency_list.items():
        text = f"{square}: {neighbors}"
        label = tk.Label(window, text=text)
        label.pack()

    # Run the tkinter event loop
    window.mainloop()