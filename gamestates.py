import pygame
import sys



pygame.init()
clock = pygame.time.Clock()


sky_blue = (127,255,212)
white = (255,255,255)
black = (0,0,0)
#different states such as main menu, levels, tutorials, source code and login

class States:
    def __init__(self):
        #setting different options
        self.menu = False
        self.level = False
        self.tutorial = False
        self.source_code = False
        self.login = False
        #


    def menu(self):
        pass




class Button:
    def __init__(self,text,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = sky_blue
        font = pygame.font.Font("neagui/font/Grand9K Pixel.ttf",25)
        self.text = font.render(text,False,white)



    def draw(self,surface):
        pos = (self.rect.x + (self.rect.width-self.text.get_width())//2,
               self.rect.y + (self.rect.height-self.text.get_width())//2)
        pygame.draw.rect(surface,self.colour,self.rect)
        surface.blit(self.text,pos)














