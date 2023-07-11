## SCRIMMAGE DURING INTERNSHIP ##

# Imports
import cv2
import pygame
import random
from pygame import mixer, font
from tinytag import TinyTag
from hollow import textOutline

# Initialize
pygame.init()
mixer.init()
font.init()

# Create fullscreen window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), )
pygame.display.set_caption("Scrimmage During Internship")

FPS = 60
clock = pygame.time.Clock()


## CLASSES ##

class Game():

    def __init__(self, player):
        """Initialize the game"""
        self.player = player
        self.frame_count = 0
        self.round_time = 0

    def update(self):
        """Update the game object"""
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0


class players(pygame.sprite.Sprite):

    def __init__(self, jump, moveleft, moveright, crouch, spawn, character, attack):
        """Initialize the player"""
        super().__init__()
        self.DEFAULT_IMAGE_SIZE = (160, 160)
        self.rightimage = pygame.transform.scale(
            pygame.image.load("Characters/" + character + "/sprites/" + character + "_Face_Right.png"),
            self.DEFAULT_IMAGE_SIZE)
        self.leftimage = pygame.transform.scale(pygame.image.load("Characters/" + character + "/sprites/" + character + "_Face_Left.png"),
                                                self.DEFAULT_IMAGE_SIZE)
        self.image = self.rightimage
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn
        self.rect.bottom = WINDOW_HEIGHT
        self.yvelocity = 8
        self.xvelocity = 0
        self.m = 1
        self.is_jump = False
        self.crouching = False
        self.crouch_height = WINDOW_HEIGHT + 90
        self.JUMP = jump
        self.MOVELEFT = moveleft
        self.MOVERIGHT = moveright
        self.CROUCH = crouch
        self.ATTACK = attack
        self.health = 100
        self.is_attack = False
        self.ATTACKCOOLDOWN = pygame.USEREVENT + 1

    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()
        self.xvelocity = 0

        # Move left and right
        if keys[self.MOVELEFT] and self.rect.left > 0:
            self.xvelocity = -6
            self.image = self.leftimage
        if keys[self.MOVERIGHT] and self.rect.right < WINDOW_WIDTH:
            self.xvelocity = 6
            self.image = self.rightimage
        if keys[self.JUMP] and self.rect.bottom == WINDOW_HEIGHT:
            self.is_jump = True
        if keys[self.CROUCH] and not self.is_jump:
            self.crouching = True

        # Jump
        if self.is_jump:
            F = (1 / 2) * self.m * (self.yvelocity ** 2)
            self.rect.y -= F
            self.yvelocity -= 1
            if self.yvelocity < 0:
                self.m = -1
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.is_jump = False
            self.yvelocity = 8
            self.rect.bottom = WINDOW_HEIGHT
            self.m = 1

        # Crouch
        if self.crouching:
            self.rect.bottom = self.crouch_height
            self.xvelocity = 0
            self.crouching = False

        # Attack
        #for event in pygame.event.get():
        #    if event.type == pygame.KEYDOWN:
        if keys[self.ATTACK] and player_1.rect.colliderect(player_2.rect):
            self.is_attack = True
        if self.is_attack:
            print("ouchie")
            self.is_attack = False

            pygame.time.set_timer(self.ATTACKCOOLDOWN, 6000)

        self.rect.x += self.xvelocity


class arena():
    pass


# Pick background
bg = cv2.VideoCapture("Assets/Backgrounds/" + str(random.randint(1, 1)) + ".mp4")
success, bg_image = bg.read()

# Pick music (ui)
bgm = "Audio/BGM/1.mp3"
now_playing_bg = pygame.image.load('Assets/UI/now playing.png')
now_playing_bg = pygame.transform.scale(now_playing_bg, (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))
mixer.music.load(bgm)
mixer.music.set_volume(1)
mixer.music.play(-1)
song_name = TinyTag.get(bgm)
print("Title: " + song_name.title)
song_font = font.Font("Assets/fonts/minecraft_font.ttf", 24)
song_title = "Now Playing: " + song_name.title
song_text = song_font.render(str(song_title), True, (0, 0, 0))
now_playing = textOutline(song_font, song_title, (0, 0, 0), (255, 255, 255))
songRect = now_playing.get_rect()
songbgRect = now_playing_bg.get_rect()
songRect.topright = (WINDOW_WIDTH, 0)
songbgRect.topright = (WINDOW_WIDTH, 0)

# Create a player group and player object
keys = pygame.key.get_pressed()
my_player_group = pygame.sprite.Group()
player_1 = players(pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s, WINDOW_WIDTH / 3, "bingo", pygame.K_z)
player_2 = players(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 2 * WINDOW_WIDTH / 3, "bingo", pygame.K_x)
my_player_group.add(player_1)
my_player_group.add(player_2)


# Main game loop
pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.event.get(player_1.ATTACKCOOLDOWN):
            print('cooldown is up')

    # Play Background
    success, bg_image = bg.read()

    bg_surf = pygame.transform.scale(pygame.image.frombuffer(bg_image.tobytes(), bg_image.shape[1::-1], "BGR"),
                                     (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Blit background
    display_surface.fill((20, 175, 175))
    display_surface.blit(bg_surf, (0, 0))

    # Blit Song title
    display_surface.blit(now_playing_bg, songbgRect)
    display_surface.blit(song_text, songRect)
    display_surface.blit(now_playing, songRect)

    # Update

    my_player_group.update()
    my_player_group.draw(display_surface)

    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
