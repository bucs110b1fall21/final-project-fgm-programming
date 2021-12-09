from src import Player
from src import Enemy
from src import Projectile

import pygame
import time
import random


class Controller:

    def __init__(self):
        self.window_width = 600
        self.window_height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load('assets/background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (600, 600))
        self.screen.blit(self.background, (0, 0))
        pygame.key.set_repeat(50, 500)

        self.player = Player.Player()
        self.enemies = []
        self.num_enemies = 4

        self.level = 0  # this is the round of the game that we are on

        self.projectiles = []
        self.EnemyProjectiles = []

        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))

    def updateScreen(self):  # updates everything that needs to be moved around on screen
        # screen updates:
        self.screen.blit(self.background, (0, 0))  # updates the background, then updates enemies, projectile, and player

        for enemy in self.enemies:  # updates each enemys location
            enemy.update(self.screen)

        self.player.update(self.screen)  # updates the player

        if len(self.projectiles) > 0:  # there are no projectiles to move it wont enter
            for projectile in self.projectiles:
                projectile.update(self.screen)  # updates the projectile
        if len(self.EnemyProjectiles) > 0:  # updates enemy projectiles
            for Eprojectile in self.EnemyProjectiles:
                Eprojectile.update(self.screen)  # updates the projectile

        # updates players lives and the level the player is on
        font = pygame.font.SysFont("ariel", 40)
        level = font.render("Level: " + str(self.level), True, (250, 250, 250))
        lives = font.render("Lives: " + str(self.player.get_lives()), True, (250, 250, 250))
        self.screen.blit(level, (5, 5))
        self.screen.blit(lives, (470, 5))

        pygame.display.flip()

    def collisions(self):
        if len(self.projectiles) > 0:  # checks to see if a player projectile has hit an enemy
            for projectile in self.projectiles:
                for enemy in self.enemies:
                    if enemy.get_rect().colliderect(projectile.get_rect()):
                        self.enemies.remove(enemy)
                        self.projectiles.remove(projectile)
                        self.updateScreen()

        if len(self.EnemyProjectiles) > 0:  # checks to see if an enemy projectile has hit the player
            for projectile in self.EnemyProjectiles:
                if self.player.get_rect().colliderect(projectile.get_rect()):
                    self.player.change_lives(-1)  # player will lose a life if he is hit
                    self.EnemyProjectiles.remove(projectile)
                    self.updateScreen()


    def mainloop(self):
        start = True
        while start:
            start_screen = pygame.image.load('assets/Start_screen.png').convert_alpha()
            start_screen = pygame.transform.scale(start_screen, (600, 600))
            introduction = pygame.image.load('assets/Instuctions.png').convert_alpha()
            self.screen.blit(start_screen, (0, 0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("wow")
                    x, y = event.pos
                    print(x)
                    print(y)
                    if (x > 163 and x < 415) and (y < 384 and y > 279):
                        start = False



        running = True
        while running:
            print("n")
            self.eventloop()  # calls event loop

            self.collisions()  # sees if any of the objects that might collide have done so

            if self.player.get_lives() <= 0:
                running = False


            if len(self.enemies) == 0:  # if there are no enemies left, this will add more and increment the level
                for x in range(self.num_enemies):
                    self.enemies.append(Enemy.Enemy(random.randint(20, 580), random.randint(-500, -100)))
                self.level += 1
                self.num_enemies += 4

            for enemy1 in self.enemies:  # if the enemy get to the bottom of the screen you lose a life
                if enemy1.get_y() > 600:
                    self.player.change_lives(-1)
                    self.enemies.remove(enemy1)

            self.updateScreen()

    def eventloop(self):
        FPS = 60
        clock = pygame.time.Clock()  # slows the game down so enemies dont move so fast
        clock.tick(FPS)

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                print("down")
                if event.key == pygame.K_a:
                    #print(event.key)
                    self.player.move("L")
                if event.key == pygame.K_d:
                    #print(event.key)
                    self.player.move("R")
                if event.key == pygame.K_SPACE:
                    #print(event.key)
                    self.projectiles.append(Projectile.Projectile(self.player.get_x() + (self.player.get_width()/2) -5,
                                                                  self.player.get_y()-15, "U"))
            elif event.type == pygame.KEYUP:
                print("up")

            for enemy in self.enemies:
                if random.randrange(0,240) == 150:
                    self.EnemyProjectiles.append(
                        Projectile.Projectile(enemy.get_x() + (enemy.get_width() / 2) - 5,
                                              enemy.get_y() + enemy.get_height(), "D"))


