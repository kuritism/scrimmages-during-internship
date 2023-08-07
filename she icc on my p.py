import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Create images...returns a Surface object with the image drawon on it.
#We can then get the rect of the surface and use the rect to position the image.
dragon_left_image = pygame.image.load("Assets/UI/Ultimatebar/0 Ult P1.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

'''dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)'''

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    #display_surface.blit(dragon_right_image, dragon_right_rect)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()
