import pygame
import sys


pygame.init()
clock = pygame.time.Clock()


sky_blue = (127, 255, 212)
white = (255, 255, 255)
black = (0, 0, 0)

#different states such as main menu, levels, tutorials, source code and login


class States:
    def __init__(self):#
        from settings import screen_width, screen_height
        #setting different options
        #menu = Menu()
        x = 500
        self.button_play = Button("Play",500,100,300,50)
        self.button_tut = Button("Tutorial",500,170,300,50)
        self.button_sc = Button("Source Code",500,240,300,50)
        self.button_leader = Button("Leaderboard",500,310,300,50)
        self.button_log = Button("Login",500,380,300,50)
        self.main_menu = False
        self.m_level = False
        self.m_tutorial = False
        self.m_source_code = False
        self.m_login = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width,screen_height))

    def menu(self):
            while self.main_menu == True:
                for event in pygame.event.get():



                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("black")
                self.button_play.draw(self.screen)
                self.button_play.collideppoint()

                self.button_tut.draw(self.screen)
                self.button_sc.draw(self.screen)
                self.button_leader.draw(self.screen)
                self.button_log.draw(self.screen)



                pygame.display.update()
                clock.tick(60)

    def level(self):
        if self.m_level == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("black")

                pygame.display.update()
                clock.tick(60)


    def tutorial(self):
        if self.m_tutorial == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("white")

                pygame.display.update()
                clock.tick(60)

    def source_code(self):
        if self.m_source_code == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("grey")

                pygame.display.update()
                clock.tick(60)

    def login(self):
        if self.m_login == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("blue")

                pygame.display.update()
                clock.tick(60)


class Button():
    def __init__(self,text,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = sky_blue
        font = pygame.font.Font("neagui/font/Grand9K Pixel.ttf",25)
        self.text = font.render(text,False,white)
        self.pressed = False
        self.click = False
        self.x = x
        self.y = y
        self.width = 300
        self.height = 50


    def draw(self,surface):
        pos = (self.rect.x + (self.rect.width-self.text.get_width())//2,
               self.rect.y + (self.rect.height-self.text.get_height())//2)
        pygame.draw.rect(surface,self.colour,self.rect)
        surface.blit(self.text,pos)

    def collideppoint(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            if self.click == False:
                self.click = True
                print("hello")


        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False









