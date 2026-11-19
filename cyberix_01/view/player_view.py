import pygame
from pathlib import Path


class PlayerView:

    def __init__(self):
        project_path = Path(__file__).resolve().parents[1]
        images_path = project_path / "assets" / "player"

        # Load the 4 player directions
        self.animations = {
            "down": pygame.image.load(
                str(images_path / "detective_front.png")
            ).convert_alpha(),
            "up": pygame.image.load(
                str(images_path / "detective_back.png")
            ).convert_alpha(),
            "left": pygame.image.load(
                str(images_path / "detective_left.png")
            ).convert_alpha(),
            "right": pygame.image.load(
                str(images_path / "detective_right.png")
            ).convert_alpha(),
        }

    def get_direction(self, player):
        if abs(player.dir_x) > abs(player.dir_y):
            if player.dir_x > 0:
                return "right"
            return "left"

        if player.dir_y > 0:
            return "down"

        if player.dir_y < 0:
            return "up"

        return "down"

    def draw(self, screen, player):
        direction = self.get_direction(player)
        image = self.animations[direction]

        render_height = int(player.size * 1.8)
        ratio = image.get_width() / image.get_height()
        render_width = int(render_height * ratio)

        image = pygame.transform.scale(image, (render_width, render_height))

        rect = image.get_rect(
            center=(
                player.x + player.size // 2,
                player.y + player.size // 2,
            )
        )

        screen.blit(image, rect)