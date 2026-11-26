
import pygame
import os

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

        self.healthbar = HealthBar(50, 5)

        self.player_view = PlayerView()
        self.monster_view = MonsterView()
        self.bullet_view = BulletView()

        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 23)
        self.title_font = pygame.font.Font(None, 38)

        # Load clue images
        self.clue_images = {}

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        clue_files = {
            "computer": "computer.png",
            "robot_part": "robot_piece.png",
            "document": "secret_note.png",
            "access_log": "entry_record.png",
            "camera": "camera.png",
            "encrypted_file": "secret_file.png"
        }

        for clue_type, filename in clue_files.items():

            image_path = os.path.join(
                project_root,
                "assets",
                "clues",
                filename
            )

            if not os.path.exists(image_path):
                raise FileNotFoundError(
                    f"Clue image not found: {image_path}"
                )

            image = pygame.image.load(
                image_path
            ).convert_alpha()

            image = pygame.transform.smoothscale(
                image,
                (64, 64)
            )

            self.clue_images[clue_type] = image

    # Draw one clue using its image
    def draw_clue(self, clue):

        image = self.clue_images.get(clue.clue_type)

        if image is None:
            return

        rect = image.get_rect(
            center=(clue.x, clue.y)
        )

        self.screen.blit(image, rect)

    # Draw all clues
    def draw_clues(self, model):

        for clue in model.level.clues:

            if not clue.collected:
                self.draw_clue(clue)

        # Nearby evidence interaction message
        if (
            model.nearby_clue is not None
            and model.active_clue is None
        ):

            message = self.small_font.render(
                f"Press E to inspect: {model.nearby_clue.name}",
                True,
                (255, 230, 120)
            )

            self.screen.blit(
                message,
                (
                    self.width // 2 - message.get_width() // 2,
                    self.height - 45
                )
            )

    # Evidence information window
    def draw_clue_info(self, model):

        clue = model.active_clue

        if clue is None:
            return

        # Dark transparent overlay
        overlay = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 175))

        self.screen.blit(overlay, (0, 0))

        # Information panel
        panel = pygame.Rect(
            120, 170, 560, 250
        )

        pygame.draw.rect(
            self.screen,
            (25, 35, 55),
            panel,
            border_radius=12
        )

        pygame.draw.rect(
            self.screen,
            (70, 180, 210),
            panel,
            2,
            border_radius=12
        )

        # Title
        title = self.title_font.render(
            clue.name,
            True,
            (100, 220, 240)
        )

        self.screen.blit(
            title,
            (150, 200)
        )

        # Description with line wrapping
        words = clue.description.split()

        lines = []
        current_line = ""

        for word in words:

            test_line = current_line + word + " "

            if self.small_font.size(test_line)[0] > 490:

                lines.append(current_line)
                current_line = word + " "

            else:
                current_line = test_line

        if current_line:
            lines.append(current_line)

        y = 260

        for line in lines:

            text = self.small_font.render(
                line,
                True,
                (230, 235, 245)
            )

            self.screen.blit(
                text,
                (150, y)
            )

            y += 28

        # Close instruction
        close_text = self.small_font.render(
            "Press ESC to close",
            True,
            (180, 190, 205)
        )

        self.screen.blit(
            close_text,
            (150, 370)
        )

    # Draw Evidence Log
    def draw_evidence_log(self, model):

        total = len(model.level.clues)

        text = self.small_font.render(
            f"Evidence: {model.collected_clues}/{total}",
            True,
            (230, 240, 255)
        )

        self.screen.blit(
            text,
            (15, 15)
        )

    # Main drawing method
    def draw(self, model):

        # Background
        model.level.background.draw(self.screen)

        # Evidence
        self.draw_clues(model)

        # Player
        self.player_view.draw(
            self.screen,
            model.player
        )

        # Normal monsters and health bars
        for monster in model.monsters:

            self.monster_view.draw(
                self.screen,
                monster
            )

            self.healthbar.draw(
                self.screen,
                monster.x,
                monster.y - 10,
                monster.health,
                monster.max_health
            )

        # Security robot
        for security in model.security_monsters:

            self.monster_view.draw(
                self.screen,
                security
            )

        # Player bullet
        self.bullet_view.draw(
            self.screen,
            model.bullet,
            "player"
        )

        # Robot bullet
        self.bullet_view.draw(
            self.screen,
            model.security_bullet,
            "robot"
        )

        # Score
        score_text = self.font.render(
            f"Score: {model.score}",
            True,
            (230, 240, 255)
        )

        self.screen.blit(
            score_text,
            (
                self.width - score_text.get_width() - 15,
                15
            )
        )

        # Evidence Log
        self.draw_evidence_log(model)

        # Evidence information
        self.draw_clue_info(model)

        pygame.display.flip()                                                                                  