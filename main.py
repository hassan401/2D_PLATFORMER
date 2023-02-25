import pygame
import sys
from settings import *
from level import Level
from player import *
from gamestates import Button
from menu import Menu

#intialising pygame and setting up essentials for game to run

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_layout, screen)


#creating objects
player = Player((32,64))
# button_play = Button("Play",500,100,300,50)

# button = Button("Play",500,100,300,50)
menu = Menu(500,90)
menu.add_button("Play")
menu.add_button("Tutorial")
menu.add_button("Source Code")
menu.add_button("Leaderboard")
menu.add_button("Login")





pygame.display.set_caption("Waddle")


# setting a loop to continuously display the screen unless user decides to quit
# where all the code from other files is compiled to make an actual running program

while True:
    for event in pygame.event.get():





        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    menu.render(screen)






    level.run()







    pygame.display.update()
    clock.tick(60)

