from src import Player
from src import Enemy
from src import Projectile

import pygame
import random
import sys


class Controller:
    def __init__(self):
        self.window_width = 900
        self.window_height = 600
        self.state = "START"
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.background.fill((250, 250, 250))
   
        pygame.font.init()
        pygame.key.set_repeat(50, 500)

        self.player = Player.Player()
        self.enemies = pygame.sprite.Group()
        for e in range(3):
            self.enemies.add(Enemy.Enemy(self.window_width, self.window_height))

        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))
    


    def mainloop(self):
          while self.state:
                if self.state == "GAME":
                    self.gameloop()
                elif self.state == "END":
                    self.endloop()
    
  
  ### below are some sample loop states ###

    def menuloop(self):
        pass
        #event loop
        #update data
        #redraw
      
    def gameloop(self):
        while self.state == "GAME":
            self.gameEventLoop()
            self.enemies.update()
            self.projectiles.update()
   
    def gameoverloop(self):
        myfont = pygame.font.SysFont(None, 30)

        if self.player.health == 0:
            self.background.fill((300, 0, 0))
            message = myfont.render('Game Over', False, (0, 0, 0))
        else:
            self.background.fill((0, 300, 0))
            message = myfont.render('Victory', False, (0, 0, 0))

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(message, (self.window_width / 2, self.window_height / 2))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

