import pygame
import math
from monster import Monster
from interfaces.fly import Flyable
from damage.rules import WeaknessDamage
class FlyingMonster(Monster , Flyable):
 def __init__(self, x, y, size, speed_x, speed_y):
    super().__init__(x, y, size, speed_x, speed_y,damage_rule=WeaknessDamage())
    self.age = 0



 def fly(self):
    self.age += 1
    self.y += math.sin(self.age / 10)

 def update(self, width, height):
    super().update(width, height)
    self.fly()

 def draw(self, screen):
    center_x = int(self.x + self.size // 2)
    center_y = int(self.y + self.size // 2)

    # Wings
    pygame.draw.ellipse(
        screen, (100, 200, 255),
        (center_x - 35, center_y - 10, 25, 15)
    )

    pygame.draw.ellipse(
        screen, (100, 200, 255),
        (center_x + 10, center_y - 10, 25, 15)
    )

    # Body
    pygame.draw.circle(
        screen, (30, 100, 200),
        (center_x, center_y), self.size // 2
    )

    # Eyes
    pygame.draw.circle(
        screen, (255, 255, 255),
        (center_x - 10, center_y - 5), 5
    )

    pygame.draw.circle(
        screen, (255, 255, 255),
        (center_x + 10, center_y - 5), 5
    )