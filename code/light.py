import pygame 
from settings import *
from debug import debug

class Light(pygame.sprite.Sprite):
    def __init__(self,state,size,pos,groups):
        super().__init__(groups)
        self.size = size
        self.state = state
        self.update()
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        if self.state == -1:
            self.image = pygame.image.load('../graphics/test/off.png').convert_alpha()
        elif self.state == 1:
            self.image = pygame.image.load('../graphics/test/on.png').convert_alpha()
