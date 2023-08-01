import pygame
import random

pygame.init()

display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("sisyphus simulator")

FPS = 2
counter = 0
clock = pygame.time.Clock()


class sis(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.distance = 0
        self.is_travel = False
        # self.image_idle = pygame.image.load()
        # self.image_move = pygame.image.load()
        # self.image = self.image_idle
        self.counter_timer = pygame.USEREVENT + 1
        self.randomevent_timer = pygame.USEREVENT + 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_travel:
            pygame.time.set_timer(self.counter_timer, 300)
            self.is_travel = True

    def randomevent(self, choice):
        pygame.time.set_timer(sisplayer.randomevent_timer, 0)

        if choice == 1:
            print("LET GO OF SPACEBAR TO FINISH GAME")
        if choice == 2:
            print('You tripped on a rock and fell')
            self.distance += random.randint(-30000000000000000000000,-10)
        if choice == 3:
            print('')

        #if self.distance < -6:
        #    self.distance = -6

        pygame.time.set_timer(self.randomevent_timer, random.randint(1000,5000))





# bg = pygame.image.load()
suffering = pygame.sprite.Group()
sisplayer = sis()
suffering.add(sisplayer)
plswork = True

running = True
while running:

    if plswork:
        pygame.time.set_timer(sisplayer.randomevent_timer, random.randint(20000,30000))
        plswork = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == sisplayer.counter_timer:
            sisplayer.distance += 1
            print(sisplayer.distance)
            sisplayer.is_travel = False
            pygame.time.set_timer(sisplayer.counter_timer, 0)

        elif event.type == pygame.KEYUP:
            sisplayer.distance = -6
            print(sisplayer.distance)
        if event.type == sisplayer.randomevent_timer and random.randint(1,1) == 1:
            sisplayer.randomevent(random.randint(1,2))






    suffering.update()
    # suffering.draw(display_surface)
