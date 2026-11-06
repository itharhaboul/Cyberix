import pygame
import math 
from interfaces.shoot import Shootable

class SecurityMonster(Shootable):

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def shoot(self, bullet, target_x, target_y):
         dx = target_x - self.x
         dy = target_y - self.y

         distance = math.hypot(dx, dy)  # calculate distance between player and mnstr

         if distance != 0:
           dir_x = dx / distance
           dir_y = dy / distance

           bullet.fire(
              self.x + self.size // 2,
              self.y + self.size // 2,
              dir_x,
              dir_y
        )
    def draw(self, screen):
      pygame.draw.rect(
        screen,
        (50, 50, 50),
        (self.x, self.y, self.size, self.size)
         )

      pygame.draw.circle(
        screen,
        (255, 0, 0),
        (self.x + self.size // 2, self.y + self.size // 2),
        8
         )