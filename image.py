import pygame
from os import walk


pygame.init()

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            f_path = path + "/" + image
            image_surf = pygame.image.load(f_path).convert_alpha()
            surface_list.append(image_surf)

        return surface_list



