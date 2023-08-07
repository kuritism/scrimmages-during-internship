import pygame
import random
from rotatefix import rot_center

pygame.init()

display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("sisyphus simulator")
font = pygame.font.SysFont('comicsansms', 32)

FPS = 60
counter = 0
clock = pygame.time.Clock()


class sis(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.distance = 0
        self.is_travel = False
        self.counter_timer = pygame.USEREVENT + 1
        self.randomevent_timer = pygame.USEREVENT + 2
        self.image = pygame.transform.scale_by(pygame.image.load("Miley.png"),2)
        self.ballimage = pygame.transform.scale_by(pygame.image.load("Meatball.png"),2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.ballimage = rot_center(self.ballimage, -45)
            if not self.is_travel:
                pygame.time.set_timer(self.counter_timer, 300)
                self.is_travel = True

    def randomevent(self, choice):
        pygame.time.set_timer(sisplayer.randomevent_timer, 0)

        if choice == 1:
            print("LET GO OF SPACEBAR TO FINISH GAME")
        if choice == 2:
            print('You tripped on a rock and fell')
            self.distance += random.randint(-20, -5)
        if choice == 3:
            print('')

        # if self.distance < -6:
        #    self.distance = -6

        pygame.time.set_timer(self.randomevent_timer, random.randint(1000, 5000))


bg = pygame.transform.scale((pygame.image.load("fancy bg.png")),(WINDOW_WIDTH,WINDOW_HEIGHT))
suffering = pygame.sprite.Group()
sisplayer = sis()
suffering.add(sisplayer)
plswork = True

playerRect = sisplayer.image.get_rect()
ballimageRect = sisplayer.ballimage.get_rect()

playerRect.center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2)
ballimageRect.center = (WINDOW_WIDTH*0.315, WINDOW_HEIGHT*0.31)

distancetext = font.render(str(sisplayer.distance), True, (255,255,255))
distancetextRect = distancetext.get_rect()
distancetextRect.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)

running = True
while running:

    if plswork:
        pygame.time.set_timer(sisplayer.randomevent_timer, random.randint(20000, 30000))
        plswork = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        distancetext = font.render(str(sisplayer.distance), True, (255,255,255))


        display_surface.blit(bg,(0,0))
        display_surface.blit(sisplayer.ballimage, ballimageRect)
        display_surface.blit(sisplayer.image, playerRect)
        display_surface.blit(distancetext, distancetextRect)


        if event.type == sisplayer.counter_timer:
            sisplayer.distance += 1
            print(sisplayer.distance)
            sisplayer.is_travel = False
            pygame.time.set_timer(sisplayer.counter_timer, 0)

        elif event.type == pygame.KEYUP and sisplayer.distance > -0:
            sisplayer.distance = 0
            print(sisplayer.distance)
        if event.type == sisplayer.randomevent_timer and random.randint(1, 1) == 1:
            sisplayer.randomevent(random.randint(1, 2))



    suffering.update()
    #suffering.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)
