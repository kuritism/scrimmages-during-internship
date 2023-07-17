## SCRIMMAGE DURING INTERNSHIP ##

# Imports
import cv2
import pygame
import random

from pygame import mixer, font
from tinytag import TinyTag
from hollow import textOutline
from grayfunc import greyscale

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
paused = False
video_loop = True

def video(read, coords, blit, path):
    """Video player function"""
    global video_loop
    video_loop = False
    try:

        success, param = read.read()
        surf = pygame.transform.scale(
            pygame.image.frombuffer(param.tobytes(), param.shape[1::-1], "BGR"),
            (coords))
        display_surface.blit(surf, blit)
    except AttributeError:
        print(path)
        print('teehee')
        video_loop = True

## CLASSES ##

class Game():

    def __init__(self, player):
        """Initialize the game"""
        self.player = player
        self.frame_count = 0
        self.round_time = 0
        self.round_number = 0
        self.score = 0

    def update(self):
        """Update the game object"""
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        # Update
        if player_1.health < 1:
            try:
                video(death, (160, 160), player_1.rect,"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
                P1_death = greyscale(player_1.playericon)
                display_surface.blit(pygame.transform.scale(P1_death, (iconcoord)), P1iconRect)
                # print('p1 dead')
                player_1.kill()


            except AttributeError:
                display_surface.blit(pygame.transform.scale(P1_death, (iconcoord)), P1iconRect)
                my_game.start_new_round(my_game)
                print('done')

        if player_2.health < 1:
            try:
                video(death, (160, 160), player_2.rect,"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
                P2_death = greyscale(player_2.playericon)
                display_surface.blit(pygame.transform.scale(P2_death, (iconcoord)), P2iconRect)
                # print('p2 dead')
                player_2.kill()

            except AttributeError:
                display_surface.blit(pygame.transform.scale(P2_death, (iconcoord)), P2iconRect)
                my_game.start_new_round(my_game)
                print('done')

        print("p1: " + str(player_1.try_ult))
        print("p2: " + str(player_2.try_ult))

        if player_1.try_ult == True:
            video(P1ultimatevideo, (WINDOW_WIDTH,WINDOW_HEIGHT),(0,0),"Characters/" + player_1.character + "/videos/" + player_1.character + "_Ultimate_Video.mp4")
            player_1.ultimate = 0
            player_1.ultbar = pygame.transform.scale_by(pygame.image.load(
                'Assets/Ultimatebar/' + str(int(round(player_1.ultimate))) + " Ult " + player_1.user + ".png"), 4)
            if video_loop == True:
                player_1.try_ult = False


        if player_2.try_ult == True:

            video(P2ultimatevideo, (WINDOW_WIDTH, WINDOW_HEIGHT),(0,0),"Characters/" + player_1.character + "/videos/" + player_1.character + "_Ultimate_Video.mp4")
            player_2.ultimate = 0
            player_2.ultbar = pygame.transform.scale_by(pygame.image.load(
                'Assets/Ultimatebar/' + str(int(round(player_2.ultimate))) + " Ult " + player_2.user + ".png"), 4)
            if video_loop == True:
                player_2.try_ult = False


    def start_new_round(self):
        # Reset variables
        self.round_time = 0
        self.frame_count = 0
        #self.round_number += 1
        print('new round')

        # Clear particles


    def pause_game(self, text, play_again):
        # Draw text
        self.game_over_text = self.font.render(text, True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        pygame.display.update()
        while paused:
            print('pause')
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False

    def reset_game(self):
        self.score = 0
        self.start_new_round()


class players(pygame.sprite.Sprite):

    def __init__(self, jump, moveleft, moveright, crouch, spawn, character, attack, user, ult):
        """Initialize the player"""
        super().__init__()
        #self.DEFAULT_IMAGE_SIZE = (160, 160)
        self.rightimage = pygame.image.load("Characters/" + character + "/sprites/" + character + "_Face_Right.png")
        self.leftimage = pygame.image.load("Characters/" + character + "/sprites/" + character + "_Face_Left.png")
        self.leftattack = pygame.image.load("Characters/" + character + "/sprites/" + character + "_Attack_Left.png")
        self.rightattack = pygame.image.load("Characters/" + character + "/sprites/" + character + "_Attack_Right.png")
        self.character = character
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
        self.ULT = ult
        #self.is_attack = False
        self.is_atkcooldown = False
        self.P1_ATTACKCOOLDOWN = pygame.USEREVENT + 1
        self.P2_ATTACKCOOLDOWN = pygame.USEREVENT + 2
        self.P1_attack_anim = pygame.USEREVENT + 3
        self.P2_attack_anim = pygame.USEREVENT + 4
        self.deal_damage = False
        self.atk_type = ""
        self.health = 100
        self.ultimate = 0
        self.user = user
        self.healthbar = pygame.image.load('Assets/Healthbar/' + str(int(round(self.health/10,0))) + " HP " + self.user + ".png")
        self.ultbar = pygame.transform.scale_by(pygame.image.load('Assets/Ultimatebar/' + str(int(round(self.ultimate))) + " Ult " + self.user + ".png"),4)
        self.playericon = pygame.transform.scale(pygame.image.load("Characters/" + character + "/sprites/" + character + "_Icon.png"),(160,160))
        self.try_ult = False


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
        if keys[self.ATTACK] and not self.is_atkcooldown :
            if self.image == self.rightimage:
                self.image = self.rightattack
            elif self.image == self.leftimage:
                self.image = self.leftattack
            if self.user == "P1":
                pygame.time.set_timer(self.P1_attack_anim, 500)
            elif self.user == "P2":
                pygame.time.set_timer(self.P2_attack_anim, 500)

            if player_1.rect.colliderect(player_2):
                self.atk_type = "BASIC"
                print(self.user + " Basic Attack")
                self.deal_damage = True
                self.is_atkcooldown = True
                if self.user == "P1":
                    pygame.time.set_timer(self.P1_ATTACKCOOLDOWN, 1000)
                    print("P1 Basic cooldown started")
                elif self.user == "P2":
                    pygame.time.set_timer(self.P2_ATTACKCOOLDOWN, 1000)



        #Ultimate
        if keys[self.ULT] and self.ultimate == 100:
            print("try ult")
            self.try_ult = True



        self.rect.x += self.xvelocity

    def takeDamage(self, atk_type):

        if atk_type == "BASIC":
            self.health -= 30
            if self.health < 0:
                self.health = 0
            print(self.user + " has " + str(self.health))
            if self.ultimate <= 100:
                self.ultimate += 100
            if self.ultimate > 100:
                self.ultimate = 100


        self.healthbar = pygame.image.load(
            'Assets/Healthbar/' + str(int(round(self.health / 10, 0))) + " HP " + self.user + ".png")
        self.ultbar = pygame.transform.scale_by(pygame.image.load(
            'Assets/Ultimatebar/' + str(int(round(self.ultimate))) + " Ult " + self.user + ".png"),4)


class arena():
    pass


# Pick background
bg = cv2.VideoCapture("Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
death = cv2.VideoCapture("Assets/death.mp4")

#success, bg_image = bg.read()
#success, death_image = death.read()
#success, player1.ultimate_image = player1.ultimate_video.read()
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
songRect.midtop = (WINDOW_WIDTH/2, 0)
songbgRect.topright = (WINDOW_WIDTH, 0)

# Create a player group and player object
my_game = Game
my_game.start_new_round(my_game),
keys = pygame.key.get_pressed()
my_player_group = pygame.sprite.Group()
player_1 = players(pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s, WINDOW_WIDTH / 3, "emu",
                   pygame.K_r, "P1", pygame.K_t)
player_2 = players(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 2 * WINDOW_WIDTH / 3, "bingo",
                   pygame.K_m, "P2", pygame.K_COMMA)
my_player_group.add(player_1)
my_player_group.add(player_2)


P1ultimatevideo = cv2.VideoCapture("Characters/" + player_1.character + "/videos/" + player_1.character + "_Ultimate_Video.mp4")
P2ultimatevideo = cv2.VideoCapture("Characters/" + player_2.character + "/videos/" + player_2.character + "_Ultimate_Video.mp4")

wait = 0
# Main game loop
pygame.mixer.music.play()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == player_1.P1_ATTACKCOOLDOWN:
            player_1.is_atkcooldown = False
            player_1.deal_damage = False
            pygame.time.set_timer(player_1.P1_ATTACKCOOLDOWN, 0)
            print('P1 Basic cooldown is up')
        if player_1.deal_damage == True:
            player_1.deal_damage = False
            #print(player_1.is_atkcooldown)
            player_2.takeDamage(player_1.atk_type)


        if event.type == player_2.P2_ATTACKCOOLDOWN:
            player_2.is_atkcooldown = False
            player_2.deal_damage = False
            pygame.time.set_timer(player_2.P2_ATTACKCOOLDOWN, 0)
            print('P2 Basic cooldown is up')
        if player_2.deal_damage == True:
            player_2.deal_damage = False
            #print(player_2.is_atkcooldown)
            player_1.takeDamage(player_2.atk_type)

        if event.type == player_1.P1_attack_anim:
            if player_1.image == player_1.rightattack:
                player_1.image = player_1.rightimage
            elif player_1.image == player_1.leftattack:
                player_1.image = player_1.leftimage

        if event.type == player_2.P2_attack_anim:
            if player_2.image == player_2.rightattack:
                player_2.image = player_2.rightimage
            elif player_2.image == player_2.leftattack:
                player_2.image = player_2.leftimage


    # HP Bar
    P1healthbarRect = (pygame.transform.scale(player_1.healthbar,(249*2,66*2)).get_rect())
    P2healthbarRect = (pygame.transform.scale(player_2.healthbar,(249*2,66*2)).get_rect())
    P1healthbarRect.topleft = (0,0)
    P2healthbarRect.topright = (WINDOW_WIDTH,0)


    P1ultbarRect = player_1.ultbar.get_rect()
    P2ultbarRect = player_2.ultbar.get_rect()
    P1ultbarRect.topleft = (P1healthbarRect.bottomleft)
    P2ultbarRect.topright = (P2healthbarRect.bottomright)


    #ICON
    iconcoord = (80,80)
    P1iconRect = (pygame.transform.scale(player_1.playericon, (iconcoord)).get_rect())
    P2iconRect = (pygame.transform.scale(player_1.playericon, (iconcoord)).get_rect())
    P1iconRect.topleft = ((WINDOW_WIDTH/200),WINDOW_HEIGHT/26.5)
    P2iconRect.topright = (WINDOW_WIDTH-(WINDOW_WIDTH/200),WINDOW_HEIGHT/26.5)

    while video_loop:

        # Play Background
        video(bg, (WINDOW_WIDTH, WINDOW_HEIGHT), (0,0),"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")

    # Blit background
    display_surface.blit(pygame.transform.scale(player_1.healthbar,(249*2,66*2)), P1healthbarRect)
    display_surface.blit(pygame.transform.scale(player_2.healthbar,(249*2,66*2)), P2healthbarRect)
    display_surface.blit(player_1.ultbar, P1ultbarRect)
    display_surface.blit(player_2.ultbar, P2ultbarRect)
    display_surface.blit(pygame.transform.scale(player_1.playericon,(iconcoord)), P1iconRect)
    display_surface.blit(pygame.transform.scale(player_2.playericon,(iconcoord)), P2iconRect)

    # Blit Song title
    #display_surface.blit(now_playing_bg, songbgRect)
    display_surface.blit(song_text, songRect)
    display_surface.blit(now_playing, songRect)
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_game.update(my_game)

    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
