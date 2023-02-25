import pygame




#loading images need to be sliced
idle_image = pygame.image.load("neagui/Sprites/01-King Human/Idle (78x58).png").convert_alpha()
attack_image = pygame.image.load("neagui/Sprites/01-King Human/Attack (78x58).png").convert_alpha()
dead_image = pygame.image.load("neagui/Sprites/01-King Human/Dead (78x58).png").convert_alpha()
#jump_image = pygame.image.load("")
run_image = pygame.image.load("neagui/Sprites/01-King Human/Run (78x58).png").convert_alpha()
hit_image = pygame.image.load("neagui/Sprites/01-King Human/Hit (78x58).png").convert_alpha()


def slice(image,button_size,size,f_size):
    image = image
    final_images = []

    buttons = slice_image(image,button_size)
    for button in buttons:
        slices = slice_image(button,size)
        create_images(slices,f_size)

    return final_images

def create_images(slices,f_size):
    surface =pygame.Surface(f_size)




def slice_image(image,size[1]):
    slices = []
    rect = image.get_rect()

    for y in range(0,rect_height,size[1]):
        for x in range(0,rect_width,size[0]):
            slices.append(image.subsurface((x,y),size))

    return slices