import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, dir):
        super().__init__()
        self.image = pygame.image.load('assets/Projectile.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed = 20
        self.dir = dir

    def get_rect(self):
        return self.rect

    def change_x(self):
        self.rect.x = 1000

    def move(self):
        if self.dir == "D":
            self.rect.y += 1
        elif self.dir == "U":
            self.rect.y -= 1

    def update(self, window):
        self.move()
        window.blit(self.image, (self.rect.x, self.rect.y))
