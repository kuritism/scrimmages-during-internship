import pygame


pygame.init()

display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("sisyphus simulator")

FPS = 2
clock = pygame.time.Clock()

class sis(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.distance = 0
        self.velocity = 0
        self.is_travel = False
        #self.image_idle = pygame.image.load()
        #self.image_move = pygame.image.load()
        #self.image = self.image_idle
        self.counter_timer = pygame.USEREVENT + 1


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_travel:
            pygame.time.set_timer(self.counter_timer, 300)
            self.is_travel = True





#bg = pygame.image.load()
suffering = pygame.sprite.Group()
sisplayer = sis()
suffering.add(sisplayer)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == sisplayer.counter_timer:
            sisplayer.distance += 1
            print(sisplayer.distance)
            sisplayer.is_travel = False
            pygame.time.set_timer(sisplayer.counter_timer, 0)


    suffering.update()
    #suffering.draw(display_surface)