import pygame
from os import walk


pygame.init()

class Assets():
    def __init__(self):
        self.black = (0,0,0)
        self.animation_list = []
        self.animation_list2 = []
        self.animation_steps = 11
        self.anim_timer = pygame.time.get_ticks()
        self.cooldown = 65
        self.frame = 0

    def show_character_idle(self):
        player_idle_sheet = self.load_image("neagui/Sprites/01-King Human/idle/Idle (78x58).png")

        for i in range(self.animation_steps):
            self.animation_list.append(self.get_image(player_idle_sheet, i, 78, 58, 1.5))

        curr_time = pygame.time.get_ticks()
        if curr_time - self.anim_timer >= self.cooldown:
            self.frame += 1
            self.anim_timer = curr_time
            if self.frame >= len(self.animation_list):
                self.frame = 0

        return self.animation_list

    def show_character_run(self):
        animation_list = []
        player_run_sheet = self.load_image("neagui/Sprites/01-King Human/run/Run (78x58).png")
        for i in range(self.animation_steps):
            animation_list.append(self.get_image(player_run_sheet, i, 78, 58, 1.5))

        return animation_list


    def load_image(self,file_path):
        return pygame.image.load(file_path).convert_alpha()

    def get_image(self, file, frame_index, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA)  # Add SRCALPHA flag
        image.blit(file, (0, 0), (frame_index * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))


        color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)

        return image

    def show_character(self):
        return {
            "idle": self.show_character_idle(),
            "run": self.show_character_run(),
            # "jump": self.show_character_jump(),
        }



