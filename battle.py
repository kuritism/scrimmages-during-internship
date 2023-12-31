## SCRIMMAGE DURING INTERNSHIP ##

# Imports
import cv2
import pygame
import random
from pyvidplayer import Video

from pygame import mixer, font
from tinytag import TinyTag
from hollow import textOutline
from grayfunc import greyscale

from crt_shader import Graphic_engine
from shadersettings import *
from pygame.locals import *

exec(open('selection.py').read())
#from selection import char_select
#char_select = ["emu", "bingo"]

# Initialize
pygame.init()
mixer.init()
font.init()

# Create fullscreen window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h
DETECTED_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)
#display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF|OPENGL)
display_surface = pygame.display.set_mode((1920, 1080), DOUBLEBUF|OPENGL)
pygame.display.set_caption("Scrimmage During Internship")

FPS = 60
clock = pygame.time.Clock()
paused = False

display_surface = pygame.Surface(VIRTUAL_RES).convert((255, 65282, 16711681, 0))
#display_surface = pygame.Surface(VIRTUAL_RES).convert((255, 65282, 16711681, 0))
# you need to give your display OPENGL flag to blit screen using OPENGL

# init shader class
crt_shader =  Graphic_engine(display_surface)

#restart_death = True
'''video_loop = 0
param = None
videoread = None'''

'''def video(read, coords, blit, path):
    """Video player function"""
    global video_loop, param, videoread
    if param is None:
        videoread = cv2.VideoCapture(path)
        success, param = videoread.read()
        video_loop +=1
    if param is not None:
        success, param = videoread.read()
        #print(videoread.read())
        surf = pygame.transform.scale(
            pygame.image.frombuffer(param.tobytes(), param.shape[1::-1], "BGR"),
            (coords))
        display_surface.blit(surf, blit)'''

P1_death = pygame.surface.Surface
P2_death = pygame.surface.Surface

## CLASSES ##

class Game():

    def __init__(self, player):
        """Initialize the game"""

        self.player = player
        self.frame_count = 0
        self.round_time = 0
        self.round_number = 0
        self.score = 0
        self.restart_death = True

    def update(self):
        """Update the game object"""
        #global P1_death, P2_death

        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        # Update
        if player_1.health < 1:
            try:
                #Video(death, (160, 160), player_1.rect,"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
                deathvideo = Video("Assets/death.mp4")
                '''if self.restart_death == True:
                    deathvideo.restart()
                    self.restart_death = False'''
                deathvideo.draw(display_surface, (player_1.rect), force_draw=False)
                #P1_death = greyscale(player_1.playericon)
                #display_surface.blit(pygame.transform.scale(P1_death, (iconcoord)), P1iconRect)
                print('p1 dead')
                player_1.kill()

            except AttributeError:
                print('done')
                deathvideo.close()
                #print(pygame.transform.scale(P1_death, (iconcoord)))
                #display_surface.blit(pygame.transform.scale(P1_death, (iconcoord)), P1iconRect)
                #my_game.start_new_round(my_game)

        if player_2.health < 1:
            try:
                #Video(death, (160, 160), player_2.rect,"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
                deathvideo = Video("Assets/death.mp4")

                '''if self.restart_death == True:
                    deathvideo.restart()
                    self.restart_death = False'''
                deathvideo.draw(display_surface, (player_2.rect), force_draw=False)
                #P2_death = greyscale(player_2.playericon)
                #display_surface.blit(pygame.transform.scale(P2_death, (iconcoord)), P2iconRect)
                print('p2 dead')
                player_2.kill()

            except AttributeError:
                print('done')
                deathvideo.close()
                #display_surface.blit(pygame.transform.scale(P2_death, (iconcoord)), P2iconRect)
                #my_game.start_new_round(my_game)



        if player_1.try_ult == True:
            try:
                #print("p1: " + str(player_1.try_ult))
                #print("p2:⠀" + str(player_2.try_ult))
                player_1.ultvideo.draw(display_surface, (0,0), force_draw=False)
                #video(P1ultimatevideo, (WINDOW_WIDTH,WINDOW_HEIGHT),(0,0),"Characters/" + player_1.character + "/videos/" + player_1.character + "_Ultimate_Video.mp4")


            except AttributeError:
                #player_1.try_ult = False
                print("vid over")
                #player_1.ultvideo.close()

            player_1.ultimate = 0
            player_1.ultbar = pygame.transform.scale_by(pygame.image.load(
                'Assets/UI/Ultimatebar/' + str(int(round(player_1.ultimate))) + " Ult " + player_1.user + ".png"), 4)



        if player_2.try_ult == True:
            try:
                #print("p1: " + str(player_1.try_ult))
                #print("p2: " + str(player_2.try_ult))
                player_2.ultvideo.draw(display_surface, (0,0), force_draw=False)
                #video(P2ultimatevideo, (WINDOW_WIDTH, WINDOW_HEIGHT),(0,0),"Characters/" + player_2.character + "/videos/" + player_2.character + "_Ultimate_Video.mp4")


            except AttributeError:
                #player_2.try_ult = False
                #player_2.ultvideo.close()
                print("vid over2")
            player_2.ultimate = 0
            player_2.ultbar = pygame.transform.scale_by(pygame.image.load(
                'Assets/UI/Ultimatebar/' + str(int(round(player_2.ultimate))) + " Ult " + player_2.user + ".png"), 4)

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
        print('?!?')
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

    def __init__(self, jump, moveleft, moveright, crouch, spawn, character, attack, user, ult, dash):
        """Initialize the player"""
        super().__init__()
        #self.DEFAULT_IMAGE_SIZE = (160, 160)
        self.rightimage = pygame.image.load(f"Characters/{character}/sprites/{character}_Face_Right.png")
        self.leftimage = pygame.image.load(f"Characters/{character}/sprites/{character}_Face_Left.png")
        self.leftattack = pygame.image.load(f"Characters/{character}/sprites/{character}_Attack_Left.png")
        self.rightattack = pygame.image.load(f"Characters/{character}/sprites/{character}_Attack_Right.png")
        self.ultvideo = Video(f"Characters/{character}/videos/{character}_Ultimate_Video.mp4")
        self.character = character
        self.image = self.rightimage
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn
        self.rect.bottom = WINDOW_HEIGHT
        self.yvelocity = 8
        self.xvelocity = 0
        self.walkvelocity = 8
        self.m = 1
        self.wm = 1
        self.is_jump = False
        self.crouching = False
        self.crouch_height = WINDOW_HEIGHT + 90
        self.JUMP = jump
        self.MOVELEFT = moveleft
        self.MOVERIGHT = moveright
        self.CROUCH = crouch
        self.ATTACK = attack
        self.ULT = ult
        self.DASH = dash
        #self.is_attack = False
        self.is_atkcooldown = False
        self.P1_ATTACKCOOLDOWN = pygame.USEREVENT + 1
        self.P2_ATTACKCOOLDOWN = pygame.USEREVENT + 2
        self.P1_attack_anim = pygame.USEREVENT + 3
        self.P2_attack_anim = pygame.USEREVENT + 4
        self.P1_DASHCOOLDOWN = pygame.USEREVENT + 5
        self.P2_DASHCOOLDOWN = pygame.USEREVENT + 6
        self.is_dashcooldown = False
        self.deal_damage = False
        self.atk_type = ""
        self.health = 100
        self.ultimate = 0
        self.user = user
        self.healthbar = pygame.image.load('Assets/UI/Healthbar/' + str(int(round(self.health/10,0))) + " HP " + self.user + ".png")
        self.ultbar = pygame.transform.scale_by(pygame.image.load('Assets/UI/Ultimatebar/' + str(int(round(self.ultimate))) + " Ult " + self.user + ".png"),4)
        self.playericon = pygame.transform.scale(pygame.image.load("Characters/" + character + "/sprites/" + character + "_Icon.png"),(160,160))
        self.try_ult = False


    def update(self):
        """Update the player"""
        global walkbob
        walkbob = 0
        keys = pygame.key.get_pressed()
        self.xvelocity = 0
        # Move left and right
        if keys[self.MOVELEFT] or keys[self.MOVERIGHT] and not self.is_jump:
            walkbob = (1 / 30) * self.wm * (self.yvelocity ** 2)
            self.rect.y -= walkbob
            self.walkvelocity -= 1
            if self.walkvelocity < 0:
                self.wm = -1
            if self.rect.bottom >= WINDOW_HEIGHT + walkbob:
                self.walkvelocity = 8
                self.wm = 1
        elif self.rect.bottom < WINDOW_WIDTH:
            self.rect.y +=4


        #fall down when no move

        if keys[self.MOVELEFT] and self.rect.left > 0:
            self.xvelocity = -12
            self.image = self.leftimage
        elif keys[self.MOVERIGHT] and self.rect.right < WINDOW_WIDTH:
            self.xvelocity = 12
            self.image = self.rightimage
        if keys[self.JUMP] and self.rect.bottom >= WINDOW_HEIGHT - 20:
            self.is_jump = True

        if keys[self.CROUCH] and not self.is_jump:
            self.crouching = True



        # Dash
        if self.is_dashcooldown == False and keys[self.DASH]:
            print(self.user + " Dash")
            if keys[self.MOVELEFT]:
                self.rect.x -= 200

            elif keys[self.MOVERIGHT]:
                self.rect.x += 200


            if self.user == "P1":
                pygame.time.set_timer(self.P1_DASHCOOLDOWN, 2000)
            if self.user == "P2":
                pygame.time.set_timer(self.P2_DASHCOOLDOWN, 2000)
            self.is_dashcooldown = True

        # Jump
        if self.is_jump:
            F = (1 / 3) * self.m * (self.yvelocity ** 2)*2
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
                    print("P2 Basic cooldown started")



        #Ultimate
        if keys[self.ULT] and self.ultimate == 100:
            print("try ult")
            self.atk_type = "ULTIMATE"
            self.deal_damage = True
            self.try_ult = True
            self.ultvideo.restart()
            self.ultvideo.resume()


        self.rect.x += self.xvelocity

    def takeDamage(self, atk_type):

        if atk_type == "BASIC":
            self.health -= 30

            if self.ultimate <= 100:
                self.ultimate += 100
            if self.ultimate > 100:
                self.ultimate = 100
        elif atk_type == "ULTIMATE":
            self.health -= 90


        if self.health < 0:
            self.health = 0
        print(self.user + " has " + str(self.health))

        self.healthbar = pygame.image.load(
            'Assets/UI/Healthbar/' + str(int(round(self.health / 10, 0))) + " HP " + self.user + ".png")
        self.ultbar = pygame.transform.scale_by(pygame.image.load(
            'Assets/UI/Ultimatebar/' + str(int(round(self.ultimate))) + " Ult " + self.user + ".png"),4)


class arena():
    pass


# Pick background
bg = cv2.VideoCapture("Assets/Backgrounds/" + str(random.randint(2, 2)) + ".mp4")
death = Video("Assets/death.mp4")
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
player_1 = players(pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s, WINDOW_WIDTH / 3, str(char_select[0]),
                   pygame.K_r, "P1", pygame.K_t, pygame.K_LSHIFT)
player_2 = players(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 2 * WINDOW_WIDTH / 3, str(char_select[1]),
                   pygame.K_m, "P2", pygame.K_COMMA, pygame.K_KP0)
my_player_group.add(player_1)
my_player_group.add(player_2)

#P1ultimatevideo = cv2.VideoCapture(
#    "Characters/" + player_1.character + "/videos/" + player_1.character + "_Ultimate_Video.mp4")
#P2ultimatevideo = cv2.VideoCapture(
#    "Characters/" + player_2.character + "/videos/" + player_2.character + "_Ultimate_Video.mp4")

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

        if event.type == player_1.P1_DASHCOOLDOWN:
            player_1.is_dashcooldown = False
            pygame.time.set_timer(player_1.P1_DASHCOOLDOWN, 0)
            print("P1 Dash cooldown is up")

        if event.type == player_2.P2_DASHCOOLDOWN:
            player_2.is_dashcooldown = False
            pygame.time.set_timer(player_2.P2_DASHCOOLDOWN, 0)
            print("P2 Dash cooldown is up")


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
    P2iconRect = (pygame.transform.scale(player_2.playericon, (iconcoord)).get_rect())
    P1iconRect.topleft = ((WINDOW_WIDTH/200),WINDOW_HEIGHT/26.5)
    P2iconRect.topright = (WINDOW_WIDTH-(WINDOW_WIDTH/200),WINDOW_HEIGHT/26.5)

    # Play Background
    #video(bg, (WINDOW_WIDTH, WINDOW_HEIGHT), (0,0),"Assets/Backgrounds/" + str(random.randint(3, 3)) + ".mp4")
    #display_surface.fill("purple")

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
    #pygame.display.update()
    crt_shader()
    clock.tick(FPS)

# End the game
pygame.quit()
