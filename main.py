import pygame
import sys
import tkinter as tk
from funct import get_adjacency_list, display_adjacency_list, assign_numbers_to_points

#V2 starts
pygame.init()
GRID_SIZE = 10
SQUARE_SIZE = 50
SCREEN_SIZE = GRID_SIZE * SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Grid Selection")

def draw_grid():
    for x in range(0, SCREEN_SIZE, SQUARE_SIZE):
        for y in range(0, SCREEN_SIZE, SQUARE_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

selected_path = []
dragging = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= SQUARE_SIZE
            y //= SQUARE_SIZE
            selected_path.append((x, y))
            dragging = True
        elif event.type == pygame.MOUSEMOTION and dragging:
            x, y = pygame.mouse.get_pos()
            x //= SQUARE_SIZE
            y //= SQUARE_SIZE
            if (x, y) not in selected_path:
                selected_path.append((x, y))
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Selected Path:", selected_path)
                running = False

    screen.fill(BLACK)
    draw_grid()

    for x, y in selected_path:
        pygame.draw.rect(screen, RED, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()
    
adjacency_list = get_adjacency_list(selected_path)

# Print the graph
for square, neighbors in adjacency_list.items():
    print(f"{square}: {neighbors}")

# Quit Pygame
pygame.quit()

#display_adjacency_list(selected_path)

# Example usage:
point_to_number, updated_adjacency_list = assign_numbers_to_points(selected_path, adjacency_list)

print("Point to Number Mapping:", point_to_number)
print("Updated Adjacency List:", updated_adjacency_list)




