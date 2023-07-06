import pygame, sys, time

pygame.init()

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
        self.rightimage = pygame.transform.scale(pygame.image.load("scrimmaging/characters/bingo/sprites/bing_Face_Right.png"), self.DEFAULT_IMAGE_SIZE)
        self.leftimage = pygame.transform.scale(pygame.image.load("scrimmaging/characters/bingo/sprites/bingo_Face_Left.png"), self.DEFAULT_IMAGE_SIZE)
        self.image = self.rightimage
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH / 2
        self.rect.bottom = WINDOW_HEIGHT
        self.yvelocity = 8
        self.xvelocity = 0
        self.m = 1
        self.is_jump = False
        self.crouching = False
        self.crouch_height = WINDOW_HEIGHT + 90

    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()
        self.xvelocity = 0

        # Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.xvelocity = -6
            self.image = self.leftimage
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.xvelocity = 6
            self.image = self.rightimage
        if keys[pygame.K_UP] and self.rect.bottom == WINDOW_HEIGHT:
            self.is_jump = True
        if keys[pygame.K_DOWN] and not self.is_jump:
            self.crouching = True

        if self.is_jump:
            F = (1 / 2) * self.m * (self.yvelocity ** 2)
            self.rect.y -= F
            self.yvelocity -= 1
            print(self.yvelocity)
            if self.yvelocity < 0:
                self.m = -1
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.is_jump = False
            self.yvelocity = 8
            self.rect.bottom = WINDOW_HEIGHT
            self.m = 1

        if self.crouching:
            self.rect.bottom = self.crouch_height
            self.xvelocity = 0
            self.crouching = False
        self.rect.x += self.xvelocity

class arena():
    pass


# Create a player group and player object
my_player_group = pygame.sprite.Group()
my_player = players()
my_player_group.add(my_player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit background
    display_surface.fill((20, 175, 175))

    # Blit text

    # Update

    my_player_group.update()
    my_player_group.draw(display_surface)

    # Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
