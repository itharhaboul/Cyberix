import pygame
from interfaces.move import Movable
from damage.rules import NormalDamage

class Monster:
     def __init__(self, x, y, size, speed_x,speed_y , damage_rule=None):
        self.x = x
        self.y = y
        self.start_x = x       # start_x et _y:when he dies,he starts again at the same place before he lose
        self.start_y = y            
        self.size = size
        self.speed_x = speed_x      
        self.speed_y = speed_y      
        self.max_health = 3         
        self.health = 3   
        self.damage_rule = damage_rule if damage_rule is not None else NormalDamage()

     def move(self):
       self.x += self.speed_x
       self.y += self.speed_y

   # direction function it depends about hawaf  
     def update(self, width, height):
        self.move()

        if self.x > width - self.size or self.x < 0:    
            self.speed_x = -self.speed_x               
        if self.y > height - self.size or self.y < 0:   
            self.speed_y = -self.speed_y                

     def hit(self, weapon):
        damage = self.damage_rule.compute(weapon)
        self.health = self.health - damage

     def respawn(self):                #  il revient à sa place
        self.x = self.start_x
        self.y = self.start_y
        self.health = self.max_health

     def draw(self, screen): 
        # Position du monstre
        center_x = int(self.x + self.size // 2)
        center_y = int(self.y + self.size // 2)
        radius = self.size // 2
        #  cornes
        pygame.draw.polygon(screen, (120, 0, 180), [
            (center_x - 15, center_y - 12),
            (center_x - 22, center_y - 30),
            (center_x - 5, center_y - 17)
        ])

        pygame.draw.polygon(screen, (120, 0, 180), [
            (center_x + 15, center_y - 12),
            (center_x + 22, center_y - 30),
            (center_x + 5, center_y - 17)
        ])
        # corps
        pygame.draw.circle(
            screen,
            (100, 30, 150),
            (center_x, center_y),
            radius
        )
        # eyes
        pygame.draw.circle(
            screen, (255, 50, 50),
            (center_x - 10, center_y - 5), 5
        )
        pygame.draw.circle(
            screen, (255, 50, 50),
            (center_x + 10, center_y - 5), 5
        )
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (center_x - 8, center_y + 12),
            (center_x + 8, center_y + 12),
            3
        )
      