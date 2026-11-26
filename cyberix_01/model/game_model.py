import math

from model.player import Player
from model.bullet import Bullet


def overlaps(ax, ay, a_size, bx, by, b_size):
    return (
        ax < bx + b_size
        and ax + a_size > bx
        and ay < by + b_size
        and ay + a_size > by
    )


class GameModel:

    def __init__(self, width, height, level):

        self.width = width
        self.height = height

        self.score = 0
        self.collected_clues = 0

        # Level created by the Builder
        self.level = level

        # Game objects
        self.player = Player(400, 300, 50, 5)

        self.bullet = Bullet(10, 10)

        # Normal monsters
        self.monsters = self.level.monsters

        # Security monsters
        self.security_monsters = self.level.security_monsters

        self.security = (
            self.security_monsters[0]
            if self.security_monsters
            else None
        )

        self.security_bullet = Bullet(10, 7)

        # Investigation system
        self.nearby_clue = None
        self.active_clue = None

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

    # Player investigates nearby evidence
    def interact(self):

        if self.nearby_clue is None:
            return

        clue = self.nearby_clue

        if not clue.collected:

            clue.collected = True
            self.active_clue = clue

            self.collected_clues = sum(
                1 for item in self.level.clues
                if item.collected
            )

    # Close evidence information
    def close_clue(self):

        self.active_clue = None

    # Detect nearby evidence
    def detect_nearby_clue(self):

        self.nearby_clue = None

        player_center_x = (
            self.player.x + self.player.size // 2
        )

        player_center_y = (
            self.player.y + self.player.size // 2
        )

        for clue in self.level.clues:

            if clue.collected:
                continue

            dx = player_center_x - clue.x
            dy = player_center_y - clue.y

            distance = math.hypot(dx, dy)

            if distance < 85:

                self.nearby_clue = clue
                break

    # Update game logic
    def update(self):

        self.bullet.update(self.width, self.height)

        # SecurityMonster detects the player
        if self.security is not None:

            dx = self.player.x - self.security.x
            dy = self.player.y - self.security.y

            distance = math.hypot(dx, dy)

            if distance < 250 and not self.security_bullet.active:

                self.security.shoot(
                    self.security_bullet,
                    self.player.x + self.player.size // 2,
                    self.player.y + self.player.size // 2
                )

        self.security_bullet.update(
            self.width, self.height
        )

        # Update normal monsters
        for monster in self.monsters:
            monster.update(self.width, self.height)

        # Collision between player bullet and monsters
        for monster in self.monsters:

            if self.bullet.active and overlaps(
                self.bullet.x,
                self.bullet.y,
                self.bullet.size,
                monster.x,
                monster.y,
                monster.size
            ):

                self.bullet.active = False

                monster.hit(self.bullet)

                if monster.health <= 0:
                    self.score += 1
                    monster.respawn()

                break

        # Investigation system
        if self.active_clue is None:
            self.detect_nearby_clue()
        else:
            self.nearby_clue = None