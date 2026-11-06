import pygame
import math
from player import Player
from monster import Monster
from bullet import Bullet
from components.healthbar import HealthBar
from monsters.fast_monster import FastMonster
from monsters.strong_monster import StrongMonster
from monsters.flying_monster import FlyingMonster
from defenses.security_monster import SecurityMonster
from components.background import Background

def overlaps(ax, ay, a_size, bx, by, b_size):
    return (ax < bx + b_size and ax + a_size > bx
            and ay < by + b_size and ay + a_size > by)


class GameBoard:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CyberiX")
        self.background = Background(self.width, self.height) ####
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.font = pygame.font.Font(None, 30)

        # Création des objets à partir des autres classes
        self.player = Player(400, 300, 50, 5)
        self.bullet = Bullet(10, 10)
        self.healthbar = HealthBar(50, 5)
        self.monsters = [
            Monster(100, 50, 50, 3, 2),
            FastMonster(200, 100, 50, 3, 2),
            StrongMonster(300, 200, 50, 2, 2),
            FlyingMonster(500, 100, 50, 2, 2) 
        ]
        self.security = SecurityMonster(700, 400, 50)
        self.security_bullet = Bullet(10, 7)   # bullet par montser

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.player.keep_inside(self.width, self.height)

        # Tir avec la touche ESPACE
        if keys[pygame.K_SPACE] and not self.bullet.active:
            start_x = self.player.x + self.player.size // 2 - self.bullet.size // 2
            start_y = self.player.y + self.player.size // 2 - self.bullet.size // 2

            self.bullet.fire(
                start_x,
                start_y,
                self.player.dir_x,
                self.player.dir_y
            )

        self.bullet.update(self.width, self.height)
        # SecurityMonster detects the player
        dx = self.player.x - self.security.x
        dy = self.player.y - self.security.y
        distance = math.hypot(dx, dy)
        if distance < 250 and not self.security_bullet.active:
         self.security.shoot(
         self.security_bullet,
         self.player.x + self.player.size // 2,
         self.player.y + self.player.size // 2
    )
        self.security_bullet.update(self.width, self.height)

      
        for monster in self.monsters:
            monster.update(self.width, self.height)

        # Collision entre la balle et les monstres
        for monster in self.monsters:
            if self.bullet.active and overlaps(
                self.bullet.x, self.bullet.y, self.bullet.size,
                monster.x, monster.y, monster.size
            ):
                self.bullet.active = False
                monster.hit(self.bullet)

                if monster.health <= 0:
                    self.score += 1
                    monster.respawn()

                break

    def draw(self):
        self.background.draw(self.screen)   
        self.player.draw(self.screen)

        for monster in self.monsters:
            monster.draw(self.screen)

            self.healthbar.draw(
                self.screen,
                monster.x,
                monster.y - 10,
                monster.health,
                monster.max_health
            )
        self.security.draw(self.screen)
        self.bullet.draw(self.screen)
        self.security_bullet.draw(self.screen)  # widnwz de security monster
        score_text = self.font.render(f"Score: {self.score}", True, (230, 240, 255))   ###
        self.screen.blit(score_text, (self.width - score_text.get_width() - 15, 15))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()