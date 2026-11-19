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

        screen.blit(self.surface, (0, 0))
        # les lumières rouges clignotent doucement
        pulse = (math.sin(pygame.time.get_ticks() / 350) + 1) / 2
        self.glow.set_alpha(int(70 + 150 * pulse))
        r = self.glow.get_width() // 2
        for x, y in self.lights:
            screen.blit(self.glow, (x - r, y - r))

