import math

from model.player import Player
from model.monster import Monster
from model.bullet import Bullet

from monsters.fast_monster import FastMonster
from monsters.strong_monster import StrongMonster
from monsters.flying_monster import FlyingMonster
from defenses.security_monster import SecurityMonster


def overlaps(ax, ay, a_size, bx, by, b_size):
    return (
        ax < bx + b_size
        and ax + a_size > bx
        and ay < by + b_size
        and ay + a_size > by
    )


class GameModel:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.score = 0

        # Game objects
        self.player = Player(400, 300, 50, 5)

        self.bullet = Bullet(10, 10)

        self.monsters = [
            Monster(100, 50, 50, 3, 2),
            FastMonster(200, 100, 50, 3, 2),
            StrongMonster(300, 200, 50, 2, 2),
            FlyingMonster(500, 100, 50, 2, 2)
        ]

        self.security = SecurityMonster(700, 400, 50)

        self.security_bullet = Bullet(10, 7)

    # Player shooting
    def shoot_player(self):

        start_x = (
            self.player.x
            + self.player.size // 2
            - self.bullet.size // 2
        )

        start_y = (
            self.player.y
            + self.player.size // 2
            - self.bullet.size // 2
        )

        self.bullet.fire(
            start_x,
            start_y,
            self.player.dir_x,
            self.player.dir_y
        )

    # Update game logic
    def update(self):

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

        # Update all monsters
        for monster in self.monsters:
            monster.update(self.width, self.height)

        # Collision between player bullet and monsters
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