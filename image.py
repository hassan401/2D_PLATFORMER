# import pygame
#
#
#
#
# # #loading images need to be sliced
# # idle_image = pygame.image.load("neagui/Sprites/01-King Human/Idle (78x58).png").convert_alpha()
# # attack_image = pygame.image.load("neagui/Sprites/01-King Human/Attack (78x58).png").convert_alpha()
# # dead_image = pygame.image.load("neagui/Sprites/01-King Human/Dead (78x58).png").convert_alpha()
# # #jump_image = pygame.image.load("")
# # run_image = pygame.image.load("neagui/Sprites/01-King Human/Run (78x58).png").convert_alpha()
# # hit_image = pygame.image.load("neagui/Sprites/01-King Human/Hit (78x58).png").convert_alpha()
#
#
# def slice(image_name,button_size,size,f_size):
#     image = pygame.image.load(image_name)
#     final_images = []
#
#     buttons = slice_image(image,button_size)
#     for button in buttons:
#         slices = slice_image(button,size)
#         final_images.append(create_images(slices,f_size))#resize image
#
#     return final_images
#
# def create_images(slices,f_size):
#     surface = pygame.Surface(f_size,pygame.SRCALPHA)
#
#     slice_width = slices[0].get.width()
#     slice_height = slices[1].get.height()
#
#     surface.blit(slices[0],(0,0))
#
#     return surface
#
#
# def slice_image(image,size):
#     slices = []
#     rect = image.get_rect()
#
#     for y in range(0,rect_height,size[1]):
#         for x in range(0,rect_width,size[0]):
#             slices.append(image.subsurface((x,y),size))
#
#     return slices
