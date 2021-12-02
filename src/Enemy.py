import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, start_range, range):
        super().__init__()
        self.image = pygame.image.load('assets/Enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = random.randrange(0, 300)
        self.dir = 'U'
        self.range = range
        self.paused = 0

    def kill(self):
        self.kill()  

    def update(self):
        pass
        
