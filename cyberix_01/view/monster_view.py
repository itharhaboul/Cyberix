import pygame
from pathlib import Path
from monsters.fast_monster import FastMonster
from monsters.strong_monster import StrongMonster
from monsters.flying_monster import FlyingMonster
from defenses.security_monster import SecurityMonster


class MonsterView:

    def __init__(self):
        project_path = Path(__file__).resolve().parents[1]
        images_path = project_path / "assets" / "monsters"

        # Normal Robot images
        normal_path = images_path / "normal"

        self.normal_images = {
            "down": pygame.image.load(
                str(normal_path / "normal_robot_front.png")
            ).convert_alpha(),

            "up": pygame.image.load(
                str(normal_path / "normal_robot_back.png")
            ).convert_alpha(),

            "left": pygame.image.load(
                str(normal_path / "normal_robot_left.png")
            ).convert_alpha(),

            "right": pygame.image.load(
                str(normal_path / "normal_robot_right.png")
            ).convert_alpha(),
        }

        # Fast Robot images
        fast_path = images_path / "fast"

        self.fast_images = {
            "down": pygame.image.load(
                str(fast_path / "fast_robot_front.png")
            ).convert_alpha(),

            "up": pygame.image.load(
                str(fast_path / "fast_robot_back.png")
            ).convert_alpha(),

            "left": pygame.image.load(
                str(fast_path / "fast_robot_left.png")
            ).convert_alpha(),

            "right": pygame.image.load(
                str(fast_path / "fast_robot_right.png")
            ).convert_alpha(),
        }

        # Strong Robot images
        strong_path = images_path / "strong"

        self.strong_images = {
            "down": pygame.image.load(
                str(strong_path / "strong_robot_front.png")
            ).convert_alpha(),

            "up": pygame.image.load(
                str(strong_path / "strong_robot_back.png")
            ).convert_alpha(),

            "left": pygame.image.load(
                str(strong_path / "strong_robot_left.png")
            ).convert_alpha(),

            "right": pygame.image.load(
                str(strong_path / "strong_robot_right.png")
            ).convert_alpha(),
        }

        # Flying Robot images
        flying_path = images_path / "flying"

        self.flying_images = {
            "down": pygame.image.load(
                str(flying_path / "flying_robot_front.png")
            ).convert_alpha(),

            "up": pygame.image.load(
                str(flying_path / "flying_robot_back.png")
            ).convert_alpha(),

            "left": pygame.image.load(
                str(flying_path / "flying_robot_left.png")
            ).convert_alpha(),

            "right": pygame.image.load(
                str(flying_path / "flying_robot_right.png")
            ).convert_alpha(),
        }

        # Security Robot image (single image, no directions)
        security_path = images_path / "security"

        self.security_image = pygame.image.load(
            str(security_path / "security_robot_front (1).png")
        ).convert_alpha()

    # Identify robot type
    def get_robot_type(self, monster):

        if isinstance(monster, FastMonster):
            return "fast"

        if isinstance(monster, StrongMonster):
            return "strong"

        if isinstance(monster, FlyingMonster):
            return "flying"

        if isinstance(monster, SecurityMonster):
            return "security"

        return "normal"

    # Determine robot direction
    def get_direction(self, monster):

        if abs(monster.speed_x) > abs(monster.speed_y):

            if monster.speed_x > 0:
                return "right"

            return "left"

        if monster.speed_y > 0:
            return "down"

        if monster.speed_y < 0:
            return "up"

        return "down"

    # Draw robot
    def draw(self, screen, monster):

        robot_type = self.get_robot_type(monster)

        # Security robot: single image, no direction
        if robot_type == "security":

            image = pygame.transform.scale(
                self.security_image,
                (monster.size * 2, monster.size * 2)
            )

            rect = image.get_rect(
                center=(
                    monster.x + monster.size // 2,
                    monster.y + monster.size // 2
                )
            )

            screen.blit(image, rect)
            return

        direction = self.get_direction(monster)

        if robot_type == "normal":
            image = self.normal_images[direction]

        elif robot_type == "fast":
            image = self.fast_images[direction]

        elif robot_type == "strong":
            image = self.strong_images[direction]

        elif robot_type == "flying":
            image = self.flying_images[direction]

        image = pygame.transform.scale(
            image,
            (monster.size * 2, monster.size * 2)
        )

        rect = image.get_rect(
            center=(
                monster.x + monster.size // 2,
                monster.y + monster.size // 2
            )
        )

        screen.blit(image, rect)