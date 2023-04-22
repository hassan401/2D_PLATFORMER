import pygame
import sys
from settings import *
from level import Level
from player import *
from gamestates import States,Button


#intialising pygame and setting up essentials for game to run

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_layout, screen)


#colours
black = (0,0,0)


#creating objects
player = Player((32,64))
button_play = Button("Play",500,100,300,50)
state = States()

state.main_menu = True


pygame.display.set_caption("Waddle")


# setting a loop to continuously display the screen unless user decides to quit
# where all the code from other files is compiled to make an actual running program

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    state.run()
    pygame.display.update()
    clock.tick(60)

