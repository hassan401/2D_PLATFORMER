import pygame


class LevelTiles(pygame.sprite.Sprite):
    def __init__(self,size,position):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = position)

    def update(self,shift):
        self.rect.x += shift