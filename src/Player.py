import pygame
import random

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = 'R'
        self.image = pygame.image.load('assets/hero.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-25, -25)
        self.speed = 10
        self.rect.x = 10
        self.rect.y = 10

    def move(self, direction):
        

