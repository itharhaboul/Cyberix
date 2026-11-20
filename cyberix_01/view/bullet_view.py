import pygame
from pathlib import Path


class BulletView:

    def __init__(self):
        project_path = Path(__file__).resolve().parents[1]
        images_path = project_path / "assets" / "bullets"

        # Player bullets
        player_path = images_path / "player"

        self.player_images = {
            "down": pygame.image.load(
                str(player_path / "player_bullet_down.png")
            ).convert_alpha(),
            "up": pygame.image.load(
                str(player_path / "player_bullet_up.png")
            ).convert_alpha(),
            "left": pygame.image.load(
                str(player_path / "player_bullet_left.png")
            ).convert_alpha(),
            "right": pygame.image.load(
                str(player_path / "player_bullet_right.png")
            ).convert_alpha(),
        }

        # Robot bullets
        robot_path = images_path / "robot"

        self.robot_images = {
            "down": pygame.image.load(
                str(robot_path / "robot_bullet_up.png")
            ).convert_alpha(),
            "up": pygame.image.load(
                str(robot_path / "robot_bullet_down.png")
            ).convert_alpha(),
            "left": pygame.image.load(
                str(robot_path / "robot_bullet_left.png")
            ).convert_alpha(),
            "right": pygame.image.load(
                str(robot_path / "robot_bullet_right.png")
            ).convert_alpha(),
        }

    # Identify bullet direction
    def get_direction(self, bullet):
        if abs(bullet.dir_x) > abs(bullet.dir_y):
            if bullet.dir_x > 0:
                return "right"
            return "left"

        if bullet.dir_y > 0:
            return "down"

        return "up"

    # Draw bullet
    def draw(self, screen, bullet, bullet_type):
        if not bullet.active:
            return

        direction = self.get_direction(bullet)

        if bullet_type == "player":
            image = self.player_images[direction]
        else:
            image = self.robot_images[direction]

        image = pygame.transform.scale(
            image,
            (bullet.size * 3, bullet.size * 3),
        )

        rect = image.get_rect(
            center=(
                bullet.x + bullet.size // 2,
                bullet.y + bullet.size // 2,
            )
        )

        screen.blit(image, rect)