import pygame
import random

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = 'D'
        self.image = pygame.image.load('assets/Player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(0, 0)
        self.speed = 10
        self.rect.x = 0
        self.rect.y = 0

    def move(self, direction):
        pass

