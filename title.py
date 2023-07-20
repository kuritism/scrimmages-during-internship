
# Imports
import pygame

# Initialize
pygame.init()

# Create fullscreen window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Draw
background = pygame.image.load('Assets/UI/Home Menu/Home Background.png')
background_rect = background.get_rect()
background_rect.topleft = (0,0)

creditz = pygame.image.load('Assets/UI/Home Menu/Home Creditz.png')
creditz_rect = creditz.get_rect()
creditz_rect.topleft = ()
