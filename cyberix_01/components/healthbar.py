import pygame
class HealthBar:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen, x, y, health, max_health):
        bar_width = int(self.width * health / max_health)
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (x, y, self.width, self.height)
        )
        pygame.draw.rect(
            screen,
            (0, 220, 50),
            (x, y, bar_width, self.height)
        )