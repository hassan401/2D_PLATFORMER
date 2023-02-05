import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = position)

    def player_movement(self):
        get_input = pygame.key.get_pressed()
        if get_input == pygame.K_w:
            pass



