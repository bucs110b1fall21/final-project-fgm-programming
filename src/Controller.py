from src import Player
from src import Enemy
from src import Projectile

import pygame
import time
import random
import shelve


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

    def display_time(self, secs): # this will be used to hold up the program so that things aren't immietatly dissapearing
        is_true = True
        start_ticks = pygame.time.get_ticks()  # starter tick
        while is_true:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
            if seconds > secs:  # if more than 10 seconds close the game
                break

    def highlight(self,old,new):  # this will make it look like the player is clicking on a button to start a game
        highlight = pygame.image.load(new).convert_alpha()
        highlight = pygame.transform.scale(highlight, (600, 600))
        self.screen.blit(highlight, (0, 0))
        pygame.display.update()
        self.display_time(1)
        cover_up = pygame.image.load(old).convert_alpha()
        cover_up = pygame.transform.scale(cover_up, (600, 600))
        self.screen.blit(cover_up, (0, 0))
        pygame.display.update()
        self.display_time(0.5)

    def mainloop(self):

        start = True
        while start:
            start_screen = pygame.image.load('assets/Start_screen.png').convert_alpha()
            start_screen = pygame.transform.scale(start_screen, (600, 600))
            self.screen.blit(start_screen, (0, 0))

            introduction = pygame.image.load('assets/Instuctions.png').convert_alpha()
            introduction = pygame.transform.scale(introduction, (600, 600))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("wow")
                    x, y = event.pos
                    print(x)
                    print(y)
                    if (x > 163 and x < 415) and (y < 384 and y > 279):  # if you click start, you enter the game loop
                        start = False
                        self.highlight('assets/Start_screen.png','assets/Start_screen_highlight.png')

                    if (x > 162 and x < 419) and (y < 564 and y > 449):
                        print("in")

                        self.highlight('assets/Start_screen.png', 'assets/Start_screen_highlight2.png')

                        intro = True
                        while(intro):  # while intro is true, we will stay stay on the intro page untill we want to leave
                            self.screen.blit(introduction, (0, 0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    exit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    x, y = event.pos
                                    if (x > 162 and x < 419) and (y < 564 and y > 449):
                                        print("in")
                                        intro = False
                                        start = False


        running = True
        while running:
            self.eventloop()  # calls event loop

            self.collisions()  # sees if any of the objects that might collide have done so

            if self.player.get_lives() <= 0:
                running = False



            if len(self.enemies) == 0:  # if there are no enemies left, this will add more and increment the level
                for x in range(self.num_enemies):
                    self.enemies.append(Enemy.Enemy(random.randint(20, 580), random.randint(-600, -100)))
                self.level += 1
                self.num_enemies += 4

            for enemy1 in self.enemies:  # if the enemy get to the bottom of the screen you lose a life
                if enemy1.get_y() > 600:
                    self.player.change_lives(-1)
                    self.enemies.remove(enemy1)

            self.updateScreen()

        if running == False:  # this is the lose screen and will show the highest score since the games creation
            endgame = pygame.image.load('assets/Gameover.png').convert_alpha()
            endgame = pygame.transform.scale(endgame, (600, 600))
            self.screen.blit(endgame, (0, 0))
            pygame.display.update()
            self.display_time(3)

            # opens a file so that we can read each line in it

            files = open('highSpace.txt', "a")
            files.writelines("," + str(self.level))
            files.close()

            high_scores = ""
            lines = open('highSpace.txt', "r")
            for line in lines:
                high_scores += line
            lines.close()


                # runs through the file to find out the highest score in the file


            font = pygame.font.SysFont("ariel", 40)
            levels = font.render("last levels reached: " + str(high_scores), True, (250, 250, 250))
            self.screen.blit(levels, (50, 50))
            pygame.display.update()
            self.display_time(3)


#########################################################################################################

    def eventloop(self):
        FPS = 60
        clock = pygame.time.Clock()  # slows the game down so enemies dont move so fast
        clock.tick(FPS)
        tick = pygame.time.get_ticks() #tics the clock so this will run 60 times every second
        last_tick = 0

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                continue
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a: #moves player sprite left or right depending on keys pressed
                    #print(event.key)
                    self.player.move("L")
                if event.key == pygame.K_d:
                    #print(event.key)
                    self.player.move("R")
                if event.key == pygame.K_SPACE: # shoots projectile if player clicks space
                    #print(event.key)

                    if tick - last_tick > 120 :
                        self.projectiles.append(Projectile.Projectile(self.player.get_x() + (self.player.get_width()/2) -5,
                                                                  self.player.get_y()-15, "U"))

            for enemy in self.enemies:  #this will randomly allow an enemy to fire usually once every 4 seconds
                if random.randrange(0,180) == 150:
                    if enemy.get_y() > -1:
                        self.EnemyProjectiles.append(Projectile.Projectile(enemy.get_x() + (enemy.get_width() / 2) - 5, enemy.get_y() + enemy.get_height(), "D"))


