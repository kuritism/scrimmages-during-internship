# simple settings
import pygame
pygame.init()
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
REAL_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)


VIRTUAL_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS=60