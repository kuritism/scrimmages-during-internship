"""WHERE DID TE BACKGROUND GO"""

# Imports
import pygame
import os
from grayfunc import greyscale

# Initialize
pygame.init()

# Create window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set values
x = 115
y = 145
select = []



for char in os.listdir("Characters"):
    # Get image
    try:
        image = pygame.image.load(f'Characters/{char}/sprites/{char}_Icon.png')
        print("Imported Character:", char)

    except FileNotFoundError:  # if file does not exist
        print(f"Error: {char} is missing sprites")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #display_surface.blit()

    # Update display
    pygame.display.update()

pygame.quit()
