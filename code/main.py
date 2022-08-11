import pygame, sys, time
from settings import *
from level import Level

class Game:
    def __init__(self):
		  
		# general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Fastlights')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        counter, text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.level.counter -= 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('grey')
            self.level.run()
            self.screen.blit(font.render(self.level.text, True, (255, 255, 255)), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
            time.sleep(0.016)

if __name__ == '__main__':
    game = Game()
    game.run()
