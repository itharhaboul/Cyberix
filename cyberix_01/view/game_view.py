import pygame

from components.background import Background
from components.healthbar import HealthBar
from view.player_view import PlayerView
from view.monster_view import MonsterView
from view.bullet_view import BulletView


class GameView:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption("CyberiX")

        self.background = Background(width, height)

        self.healthbar = HealthBar(50, 5)

        self.player_view = PlayerView()
        self.font = pygame.font.Font(None, 30)
        self.monster_view = MonsterView()
        self.bullet_view = BulletView()

    def draw(self, model):
        # Background
        self.background.draw(self.screen)

        # Player
        self.player_view.draw(self.screen, model.player)

        # Monsters and their health bars
        for monster in model.monsters:
            self.monster_view.draw(self.screen, monster)

            self.healthbar.draw(
                self.screen,
                monster.x,
                monster.y - 10,
                monster.health,
                monster.max_health,
            )

        # Security robot
        if model.security is not None:
            self.monster_view.draw(self.screen, model.security)

        # Player bullet
        self.bullet_view.draw(
            self.screen,
            model.bullet,
            "player",
        )

        # Robot bullet
        self.bullet_view.draw(
            self.screen,
            model.security_bullet,
            "robot",
        )

        # Score
        score_text = self.font.render(
            f"Score: {model.score}",
            True,
            (230, 240, 255),
        )

        self.screen.blit(
            score_text,
            (self.width - score_text.get_width() - 15, 15),
        )

        pygame.display.flip()