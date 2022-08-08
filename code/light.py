import pygame 
from settings import *
from debug import debug

class Light(pygame.sprite.Sprite):
    def __init__(self,state,pos,groups):
        super().__init__(groups)
        if state == 0:
            self.image = pygame.image.load('../graphics/test/off.png').convert_alpha()
        elif state == 1:
            self.image = pygame.image.load('../graphics/test/on.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def input(self):
        click = pygame.mouse.get_pressed()
        if click:
            mousepos = pygame.mouse.get_pos()

