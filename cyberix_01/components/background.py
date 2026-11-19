import pygame
from pathlib import Path


class Background:

    def __init__(self, width, height):

        project_path = Path(__file__).resolve().parents[1]

        image_path = project_path / "assets" / "backgrounds" / "laboratory.png"

        self.image = pygame.image.load(str(image_path)).convert()

        # Resize background
        self.image = pygame.transform.scale(
            self.image,
            (width, height)
        )

    def draw(self, screen):

        screen.blit(self.image, (0, 0))