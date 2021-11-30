import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, limit):
        super().__init__()
        self.image = pygame.image.load('assets/projectile.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.limit = limit
        self.speed = 10
    
    def update(self):
        self.rect.x += self.speed

        if self.rect.x > self.limit:
            self.kill()

