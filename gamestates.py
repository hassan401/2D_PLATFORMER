import pygame
import sys
from pygame.locals import *
from level import Level
from settings import *


pygame.init()
clock = pygame.time.Clock()


sky_blue = (127, 255, 212)
white = (255, 255, 255)
black = (0, 0, 0)

#different states such as main menu, levels, tutorials, source code and login


class States:
    def __init__(self):#
        from settings import screen_width, screen_height

        x = 500
        self.button_play = Button("Play",500,100,300,50)
        self.button_tut = Button("Tutorial",500,170,300,50)
        self.button_sc = Button("Source Code",500,240,300,50)
        self.button_leader = Button("Leaderboard",500,310,300,50)
        self.button_log = Button("Login",500,380,300,50)
        self.button_section1 = Button("Section 1",500,380,300,50)
        self.button_section2 = Button("Section 2",500,380,300,50)
        self.button_level1 = Button("Level 1",500,380,300,50)
        self.button_level2 = Button("Level 2",500,380,300,50)
        self.button_level3 = Button("Level 3",500,380,300,50)
        self.main_menu = False
        self.m_level = False
        self.m_tutorial = False
        self.m_source_code = False
        self.m_leaderboard = False
        self.m_login = False
        self.m_p_level = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width,screen_height))


    def run(self):
        if self.main_menu:
            return self.menu()
        elif self.m_level:
            return self.level()
        elif self.m_tutorial:
            return self.tutorial()
        elif self.m_source_code:
            return self.source_code()
        elif self.m_login:
            return self.login()
        elif self.m_leaderboard:
            return self.leaderboard()
        elif self.m_p_level:
            return self.m_p_level()


    def display_buttons(self):
        self.button_play.draw(self.screen)
        self.button_tut.draw(self.screen)
        self.button_sc.draw(self.screen)
        self.button_leader.draw(self.screen)
        self.button_log.draw(self.screen)

    def button_collision_handler(self):
        if self.button_play.collideppoint():
            self.main_menu = False
            self.m_level = True

        if self.button_tut.collideppoint():
            self.main_menu = False
            self.m_tutorial = True

        if self.button_sc.collideppoint():
            self.main_menu = False
            self.m_source_code = True

        if self.button_leader.collideppoint():
            self.main_menu = False
            self.m_leaderboard = True

        if self.button_log.collideppoint():
            self.main_menu = False
            self.m_login = True


    def menu(self):
        while self.main_menu == True:
            for event in pygame.event.get():
                self.button_collision_handler()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill("black")
            self.display_buttons()
            pygame.display.update()
            clock.tick(60)
            if not self.main_menu:
                break
        return self.run()


    def level(self):
        level = Level(level_layout, self.screen)
        if self.m_level == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_level = False
                            self.main_menu = True

                self.screen.fill("blue")
                level.run()



                pygame.display.update()
                clock.tick(60)
                if not self.m_level:
                    break
            return self.run()


    def tutorial(self):
        if self.m_tutorial == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_tutorial = False
                            self.main_menu = True
                self.screen.fill("white")

                pygame.display.update()
                clock.tick(60)
                if not self.m_tutorial:
                    break
            return self.run()

    def source_code(self):
        if self.m_source_code == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_source_code = False
                            self.main_menu = True
                self.screen.fill("grey")

                pygame.display.update()
                clock.tick(60)
                if not self.m_source_code:
                    break
            return self.run()


    def leaderboard(self):
        if self.m_leaderboard == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_leaderboard = False
                            self.main_menu = True
                self.screen.fill("blue")

                pygame.display.update()
                clock.tick(60)
                if not self.m_leaderboard:
                    break
            return self.run()


    def login(self):
        if self.m_login == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_login = False
                            self.main_menu = True
                self.screen.fill("green")

                pygame.display.update()
                clock.tick(60)
                if not self.m_login:
                    break
            return self.run()

    def play_sections(self):
        if self.m_p_section == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_p_section = False
                            self.m_level = True
                self.screen.fill("green")

                pygame.display.update()
                clock.tick(60)
                if not self.m_p_level:
                    break
            return self.run()

    def play_levels(self):
        if self.m_p_level == True:
            while True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.m_p_level = False
                            self.m_p_section  = True
                self.screen.fill("sky blue")

                pygame.display.update()
                clock.tick(60)
                if not self.m_p_level:
                    break
            return self.run()


class Button():
    def __init__(self,text,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = sky_blue
        font = pygame.font.Font("neagui/font/Grand9K Pixel.ttf",25)
        self.text = font.render(text,False,white)
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
        pressed = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            if self.click == False:
                self.click = True
                pressed = True



        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        return pressed









