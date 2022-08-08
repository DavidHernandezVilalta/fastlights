import pygame 
from settings import *
from light import Light
from debug import debug
from random import randrange

class Level:
    def __init__(self):

		# get the display surface 
        self.display_surface = pygame.display.get_surface()

		# sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
        self.create_map()

    def create_map(self):
        for i in range(10):
            rand_row = randrange(MAX_ROWS)
            rand_cols = randrange(MAX_COLS)
            WORLD_MAP[rand_row][rand_cols] = 1

        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 1:
                    Light (1, 64, (x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 0:
                    Light (0, 64, (x,y),[self.visible_sprites,self.obstacle_sprites])
        print(self.obstacle_sprites.sprites()[0].size)

    def input(self):
        click = pygame.mouse.get_pressed()[0]
        if click:
            mousex = pygame.mouse.get_pos()[0]
            mousey = pygame.mouse.get_pos()[1]
            row = mousex // 64;
            col = mousey // 64;
            print(self.obstacle_sprites.sprites()[col*MAX_COLS+row].state)

    def run(self):
		# update and draw the game
        self.input()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
