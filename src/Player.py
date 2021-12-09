import pygame
import random


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = 'D'
        self.image = pygame.image.load('assets/Player.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # self.rect.inflate_ip(0, 0)
        self.speed = 20
        self.rect.x = 10
        self.rect.y = 550
        self.lives = 3

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def get_lives(self):
        return self.lives  # can get the amount of lives the player has left

    def change_lives(self, x):
        self.lives += x  # can change the amount of lives the player has

    def check_boundary(self):  # makes sure the player is within the window and on the screen
        if self.rect.x < 0:  # boundaries for where a player can move to
            self.rect.x += self.speed
            # print("L ", self.rect.x )
        elif self.rect.x > (600 - self.image.get_width()):
            self.rect.x -= self.speed
            # print("R ", self.rect.x )

    def move(self, direction):

        if direction == "L":  # allows a player to move left and right
            self.rect.x -= self.speed
            # print("L-",self.rect.x)
        elif direction == "R":
            self.rect.x += self.speed
            # print("R-",self.rect.x)
        self.check_boundary()

    def update(self, window):
        self.check_boundary()
        window.blit(self.image, (self.rect.x, self.rect.y))
