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
pygame.display.set_caption("Choose your Character")

# Set values
x = 115
y = 145
char_select = []
icon_offset = 0
count = 0

class Icon:
    def __init__(self, chara):
        self.image = pygame.transform.scale(pygame.image.load(f'Characters/{chara}/sprites/{chara}_Icon.png'), (240, 240))
        self.rect = self.image.get_rect()
        self.count = 1
        self.gcount = 1
        self.chara = chara

    def myfunc(self, mouse):
        if self.rect.collidepoint(mouse):
            return True

    def blitfunc(self):
        global icon_offset, count

        if self.count == 1:
            self.rect.topleft = (icon_offset + 120, 240)
            icon_offset += 240
            self.count += 1

        display_surface.blit(self.image, self.rect)

    def blitgrayfunc(self):
        global icon_offset, count
        self.image = greyscale(self.image)


bingo = Icon("bingo")
emu = Icon("emu")
petticoat = Icon("petticoat")
tbh = Icon("tbh")
chars = [bingo, emu, petticoat, tbh]
char_count = 0
clickcount = 0

for char in os.listdir("Characters"):
    # Get image
    try:
        # image = pygame.image.load(f'Characters/{char}/sprites/{char}_Icon.png')
        #char_select.append(char)
        print(char)
        #char_select[char_count] = Icon(char)
        print("Imported Character:", char)
        char_count += 1
        # char = Icon(str(char))

    except FileNotFoundError:  # if file does not exist
        print(f"Error: {char} is missing sprites")

background = pygame.image.load('Assets/UI/Character Selection/Player 1 Select.png')
background_rect = background.get_rect()
background_rect.topleft = (0, 0)

play = pygame.transform.scale(pygame.image.load('Assets/UI/Character Selection/Start.png'), (600, 300))
play_rect = play.get_rect()
play_rect.bottomright = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Main loop
running = True
ready = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for e in chars:
            if e.myfunc(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    char_select.append(e.chara)
                    clickcount += 1
                    background = pygame.image.load('Assets/UI/Character Selection/Player 2 Select.png')
                    background_rect = background.get_rect()
                    pygame.display.update()
                print('hove')

            if play_rect.collidepoint(pygame.mouse.get_pos()):
                running = False


    display_surface.blit(background, background_rect)

    # Blit images
    for e in chars:
        e.blitfunc()

    if clickcount > 1:
        for e in chars:
            e.blitgrayfunc()
        display_surface.blit(play, play_rect)

    # Update display
    pygame.display.update()

pygame.quit()
