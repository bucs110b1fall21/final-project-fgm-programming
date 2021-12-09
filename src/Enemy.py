import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y):
        super().__init__()
        self.image = pygame.image.load('assets/Enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.dir = 'R'
        self.switch = 0  # tells the enemies when they should switch direction

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def get_rect(self):
        return self.rect

    def move(self):
        # print(self.rect.y)
        self.rect.y += 1  # lowers the enemy sprites by 2 each time they are updated
        # print(self.rect.y)
        self.switch += 1  # this is count for when the enemy switches direction

        # print(self.rect.x)
        if ((self.rect.x + self.image.get_width()) >= 599):
            self.dir = "L"
            self.rect.x -= 1
            self.switch = 0
        elif self.rect.x <= 1:
            self.dir = "R"
            self.rect.x += 1
        else:
            if self.switch > 50:
                if self.dir == "R":  # every 50, enemies will switch direction
                    self.dir = "L"
                    self.switch = 0
                elif self.dir == "L":
                    self.dir = "R"
                    self.switch = 0

        if self.dir == "R":  # moves the enemy left or right depending on its direction
            self.rect.x += 1
            # print("R ",self.rect.x)
        elif self.dir == "L":
            self.rect.x -= 1
            # print("L ",self.rect.x)

        self.switch += 1

    def update(self, window):
        self.move()
        window.blit(self.image, (self.rect.x, self.rect.y))


        
