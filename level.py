import pygame
from leveltiles import LevelTiles
from settings import tile_size
from player import Player
from settings import screen_width

# class Level uses a method to set up the level by placing rects at positions where x would appear

class Level:
    def __init__(self,level_data,screen):
        self.setup_level(level_data)
        self.display = screen
        self.shift = 0


    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = LevelTiles(tile_size,(x,y))
                    self.tiles.add(tile)
                elif col == "P":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player = Player((x,y))
                    self.player.add(player)


    def camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        move_x = player.move.x

        if player_x < (screen_width /4) and move_x < 0:
            self.shift = 7
            player.speed = 0
        elif player_x > ((screen_width /4)*3) and move_x > 0:
            self.shift = -7
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 7




    def run(self):
        self.player.draw(self.display)
        self.player.update()
        self.tiles.draw(self.display)
        self.camera()


        self.tiles.update(self.shift)