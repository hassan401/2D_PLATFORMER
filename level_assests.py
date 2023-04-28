import pygame

class Levelassets():
    def __init__(self,screen):
        self.screen = screen
        self.coin = pygame.image.load("neagui/Sprites/12-Live and Coins/01.png")
        self.coin = pygame.transform.scale(self.coin,(40,40))
        self.health = pygame.image.load("neagui/Sprites/12-Live and Coins/Live Bar.png")

    def draw_coin(self):

        self.screen.blit(self.coin,(100,10))

    def draw_health(self):
        self.screen.blit(self.health,(10,10))






