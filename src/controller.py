from src import Player
from src import Enemy
from src import Projectile

import pygame

class Controller:

    def __init__(self):
        self.window_width = 1000
        self.window_height = 500
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.background.fill((250, 250, 250))
        pygame.key.set_repeat(50, 500)

        self.player = Player.Player()
        self.enemies = pygame.sprite.Group()
        for e in range(3):
            self.enemies.add(Enemy.Enemy(self.window_width, self.window_height))

        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))

    def mainloop(self):
        while True:  
            self.eventloop()

            self.enemies.update()
            self.projectiles.update()

            bullets = pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)
            if bullets:
                for enemy in bullets:
                    enemy.pause()

            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move("L")
                if event.key == pygame.K_RIGHT:
                    self.player.move("R")
                if event.key == pygame.K_SPACE:
                    if len(self.projectiles.sprites()) <= 5:
                        p = Projectile.Projectile(self.window_width)
                        pos = self.player.rect.midright
                        p.rect.x = pos[0]
                        p.rect.y = pos[1]
                        self.projectiles.add(p)
                        self.all_sprites(p)
                    else:
                        print("can't shoot", len(self.projectiles.sprites()))

