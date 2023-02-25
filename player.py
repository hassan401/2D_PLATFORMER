import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__() #inheriting here so need this
        # self.image = pygame.Surface((32,64))
        # self.image.fill("red")
        self.image = pygame.image.load("neagui/Sprites/01-King Human/Ground (78x58).png ").convert_alpha()
        self.move = pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect(topleft = position)
        self.speed = 7
        self.gravity = 0.8
        self.jump = -15



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



    def apply_gravity(self):
        self.move.y += self.gravity
        self.rect.y += self.move.y






    def update(self):
        self.rect.x += self.move.x * self.speed
        self.player_movement()
        self.apply_gravity()



