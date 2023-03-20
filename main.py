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


#creating objects
player = Player((32,64))

button_play = Button("Play",500,100,300,50)


button = Button("Play",500,100,300,50)
button.add_button("Play")
button.add_button("Tutorial")
button.add_button("Source Code")
button.add_button("Leaderboard")
button.add_button("Login")


state = States()



pygame.display.set_caption("Waddle")


# setting a loop to continuously display the screen unless user decides to quit
# where all the code from other files is compiled to make an actual running program

while True:
    for event in pygame.event.get():
        state.menu()
        state.tutorial()
        state.source_code()
        state.login()











        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")

    button.render(screen)






    level.run()







    pygame.display.update()
    clock.tick(60)

