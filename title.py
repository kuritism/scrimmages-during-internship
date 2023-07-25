
# Imports
import pygame
import ctypes

# Initialize
pygame.init()

# Create fullscreen window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Draw
background = pygame.image.load('Assets/UI/Home Menu/Titlescreen.png')
background_rect = background.get_rect()
background_rect.topleft = (0, 0)

menu = pygame.transform.scale_by(pygame.image.load('Assets/UI/Home Menu/Home Menu.png'), 0.8)
menu_rect = menu.get_rect()
menu_rect.bottomleft = (0, WINDOW_HEIGHT)

play = pygame.transform.scale_by(pygame.image.load('Assets/UI/Home Menu/Home Play.png'), 0.8)
play_rect = play.get_rect()
play_rect.topleft = (0, 420)

settings = pygame.transform.scale_by(pygame.image.load('Assets/UI/Home Menu/Home Settings.png'), 0.8)
settings_rect = settings.get_rect()
settings_rect.topleft = (0, 700)

creditz = pygame.transform.scale_by(pygame.image.load('Assets/UI/Home Menu/Home Creditz.png'), 0.8)
creditz_rect = creditz.get_rect()
creditz_rect.bottomleft = (0, WINDOW_HEIGHT)

# Main game loop
window = False
running = True
clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked = True
            if play_rect.collidepoint(mouse_x, mouse_y):
                print('play')
                exec(open('selection.py').read())
            elif settings_rect.collidepoint(mouse_x, mouse_y):
                print('settings')
            elif creditz_rect.collidepoint(mouse_x, mouse_y):
                print('credirz')

    # Blit
    display_surface.blit(background, background_rect)

    if clicked:
        if not window:
            ctypes.windll.user32.MessageBoxW(0, "This game was made in mind to be played in a healthy manner! This "
                                                "game will regularly pause the game at intervals for water breaks and "
                                                "give out reminders during long playtime!", "Notice!", 1)
            window = True
        background = pygame.image.load('Assets/UI/Home Menu/Home Background.png')
        display_surface.blit(background, background_rect)
        display_surface.blit(menu, menu_rect)
        display_surface.blit(play, play_rect)
        display_surface.blit(settings, settings_rect)
        display_surface.blit(creditz, creditz_rect)

    # Update the display
    pygame.display.update()

pygame.quit()
