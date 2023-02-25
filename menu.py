import pygame
from gamestates import Button



class Menu:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 50
        self.buttons = []

    def add_button(self,text):
        self.buttons.append(Button(text,self.x,self.y,self.width,self.height))
        self.y = self.height + 10

    def render(self,surface):
        for button in self.buttons:
            button.render(surface)
