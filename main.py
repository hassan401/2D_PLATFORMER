import pygame
import sys
from settings import *
from level import Level
from player import Player

#intialising pygame and setting up essentials for game to run

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level1, screen)
pygame.display.set_caption("Waddle")


# setting a loop to continuously display the screen unless user decides to quit
# where all the code from other files is compiled to make an actual running program

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    level.run()
    

    pygame.display.update()
    clock.tick(60)

