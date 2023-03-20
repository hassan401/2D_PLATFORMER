import pygame
from image import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__() #inheriting here so need this
        self.player_assests()
        self.image = pygame.Surface((32,64))
        self.image.fill("gold")
        #self.image = pygame.image.load("neagui/Sprites/01-King Human/Ground (78x58).png ").convert_alpha()
        self.move = pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect(topleft = position)
        self.speed = 5
        self.gravity = 0.8
        self.jump = -10
        self.jump_counter = 0

# here in player movement i use vectors to move the player rects
    def player_movement(self):
        get_input = pygame.key.get_pressed()
        if get_input[pygame.K_a]:
            self.move.x = -1
        elif get_input[pygame.K_d]:
            self.move.x = 1
        else:
            self.move.x = 0

        if get_input[pygame.K_SPACE]:
                self.move.y = self.jump

    def player_assests(self):
        sprite_path = "../neagui/Sprites/01-King Human/"
        self.animations = {"idle":[],"attack":[],"jump":[],"":[],"ground":[],"hit":[],"dead":[],"fall":[],"run":[]}

        for animations in self.animations.keys():
            path = sprite_path + animations
            self.animations[animations] = import_folder(path)

    def apply_gravity(self):
        self.move.y += self.gravity
        self.rect.y += self.move.y

    def update(self):
        self.player_movement()
        self.apply_gravity()



