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
        self.button = Button("Play",500,100,300,50)
        self.main_menu = False
        self.m_level = False
        self.m_tutorial = False
        self.m_source_code = False
        self.m_login = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width,screen_height))

    def menu(self):
        if self.main_menu == True:
            while True:
                for event in pygame.event.get():
                    self.state.menu()


                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.screen.fill("black")
                self.button.render(screen)

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
        self.x = x
        self.y = y
        self.width = 300
        self.height = 50
        self.buttons = []

    def collide_button(self):
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                print("clcik")
            else:
                self.pressed = False

    def draw(self,surface):


        pos = (self.rect.x + (self.rect.width-self.text.get_width())//2,
               self.rect.y + (self.rect.height-self.text.get_height())//2)
        pygame.draw.rect(surface,self.colour,self.rect)
        surface.blit(self.text,pos)
        self.collide_button()


    def add_button(self,text):
        self.buttons.append(Button(text,self.x,self.y,self.width,self.height))
        self.y += self.height + 10


    def render(self,surface):
        for button in self.buttons:
            button.draw(surface)








