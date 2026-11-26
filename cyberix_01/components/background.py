import pygame
import math
from pathlib import Path


class Background:

    def __init__(self, width, height, image_name="laboratory.png"):

        project_path = Path(__file__).resolve().parents[1]

        image_path = (
            project_path / "assets" / "backgrounds" / image_name
        )

        self.image = pygame.image.load(
            str(image_path)
        ).convert()

        self.image = pygame.transform.scale(
            self.image,
            (width, height)
        )

        # Create red glow effect
        self.glow = pygame.Surface(
            (100, 100),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            self.glow,
            (255, 0, 0, 15),
            (50, 50),
            50
        )

        pygame.draw.circle(
            self.glow,
            (255, 0, 0, 30),
            (50, 50),
            35
        )

        pygame.draw.circle(
            self.glow,
            (255, 30, 30, 60),
            (50, 50),
            20
        )

        pygame.draw.circle(
            self.glow,
            (255, 50, 50, 100),
            (50, 50),
            8
        )

        # Red warning lights positions
        self.lights = [
            (100, 80),
            (700, 80),
            (100, 500),
            (700, 500)
        ]

    def draw(self, screen):

        # Draw background
        screen.blit(self.image, (0, 0))

        # Pulsing effect
        pulse = (
            math.sin(pygame.time.get_ticks() / 350) + 1
        ) / 2

        self.glow.set_alpha(
            int(70 + 150 * pulse)
        )

        radius = self.glow.get_width() // 2

        for x, y in self.lights:

            screen.blit(
                self.glow,
                (x - radius, y - radius)
            )