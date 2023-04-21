import pygame
from image import Assets


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.assets = Assets()
        self.current_state = "idle"
        self.is_grounded = False
        self.animation_states = self.assets.show_character()
        self.update_animation_list()
        self.frame_index = 0
        self.image = self.animation_list[self.frame_index]
        self.anim_timer = pygame.time.get_ticks()
        self.anim_cooldown = 65
        self.move = pygame.math.Vector2(0, 0)
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 5
        self.gravity = 0.8
        self.jump = -10
        self.jump_counter = 0

    def player_movement(self):
        get_input = pygame.key.get_pressed()
        self.move_left = self.move_right = self.move_idle = self.move_jump = False

        if get_input[pygame.K_a]:
            self.move.x = -1
            self.move_left = True
        elif get_input[pygame.K_d]:
            self.move.x = 1
            self.move_right = True
        else:
            self.move.x = 0
            self.move_idle = True

        if get_input[pygame.K_SPACE]:
            self.move.y = self.jump
            self.move_jump = True


        prev_state = self.current_state
        if self.move.x < 0 or self.move.x > 0:
            self.current_state = "run"
        else:
            self.current_state = "idle"

        if prev_state != self.current_state:
            self.update_animation_list()

    def update_animation_list(self):
        self.animation_list = self.animation_states[self.current_state].copy()
        if self.current_state == "run" and self.move.x < 0:
            for i, frame in enumerate(self.animation_list):
                self.animation_list[i] = pygame.transform.flip(frame, True, False)

    def get_frame(self):
        curr_time = pygame.time.get_ticks()
        if curr_time - self.anim_timer >= self.anim_cooldown:
            self.frame_index += 1
            self.anim_timer = curr_time
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0

        prev_rect = self.rect
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect(topleft=prev_rect.topleft)

    def apply_gravity(self):
        self.move.y += self.gravity
        self.rect.y += self.move.y

        if self.rect.y >= 0:
            self.is_grounded = True
        else:
            self.is_grounded = False

    def update(self):
        self.player_movement()
        self.apply_gravity()
        self.get_frame()
