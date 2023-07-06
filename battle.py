import cv2
import pygame, sys, time, random
from pygame import mixer
from tinytag import TinyTag

pygame.init()
mixer.init
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Scrimmage During Internship")



FPS = 60
clock = pygame.time.Clock()


class Game():

    def __init__(self, player):
        """Initialize the game"""
        self.player = my_player
        self.frame_count = 0
        self.round_time = 0

    def update(self):
        """Update the game object"""
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0


class players(pygame.sprite.Sprite):



    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.DEFAULT_IMAGE_SIZE = (160, 160)
        self.image = pygame.transform.scale(pygame.image.load("Characters/bingo/bing_Face_Right.png"), self.DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH / 2
        self.rect.bottom = WINDOW_HEIGHT


        self.velocity = 8

    def update(self):
        """Update the player"""
        a = 0

        keys = pygame.key.get_pressed()

        # Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.bottom == WINDOW_HEIGHT:
            """JUMPSTART = int(round(time.time()*1000))
            JUMP = True
            while JUMP == True:

                TIMEPASSED = int(round(time.time()*1000)) - JUMPSTART
                if TIMEPASSED <= 2000:
                    self.rect.y -= 1
                if TIMEPASSED == 2:
                    JUMP = False"""
            
            last_time_ms = int(round(time.time() * 1000))
            while a <= 3:
                diff_time_ms = int(round(time.time() * 1000)) - last_time_ms
                if diff_time_ms >= 1000:
                    a += 1
                    last_time_ms = int(round(time.time() * 1000))
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                # display_surface.blit(pygame.image.load(images[a]).convert(),(0,0))
                #display_surface.blit(pygame.image.load("bing_Face_Right.png").convert(), (0, 0))

                display_surface.fill((20, 175, 175))
                print(a)
                my_player_group.update()
                my_player_group.draw(display_surface)
                pygame.display.update()


class arena():
    pass


# Create a player group and player object
my_player_group = pygame.sprite.Group()
my_player = players()
my_player_group.add(my_player)

# Pick background
bg = cv2.VideoCapture("Assets/Backgrounds/" + str(random.randint(1, 1)) + ".mp4")
success, bg_image = bg.read()
bg_fps = bg.get(cv2.CAP_PROP_FPS)
bg_clock = pygame.time.Clock()

# Pick music
mixer.music.load("audio/BGM/" + str(random.randint(1, 1)) + ".mp3")
mixer.music.set_volume(0.7)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Play Music

    mixer.music.play(-1)

    # Play Background
    bg_clock.tick(bg_fps)
    success, bg_image = bg.read()

    bg_surf = pygame.image.frombuffer(bg_image.tobytes(), bg_image.shape[1::-1], "BGR")



    # Blit background
    display_surface.blit(bg_surf, (160, 0))

    # Blit text

    # Update

    my_player_group.update()
    my_player_group.draw(display_surface)

    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
