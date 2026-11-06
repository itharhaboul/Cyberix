import pygame
class Bullet:
    def __init__(self, size, speed,damage=1):
        self.x = 0 
        self.y = 0
        self.size = size
        self.speed = speed
        self.damage = damage
        self.dir_x = 0               # to can manage all direction of bullets
        self.dir_y = -1           
        self.active = False

    def fire(self, x, y ,dir_x,dir_y):
        self.active = True
        self.x = x
        self.y = y
        self.dir_x = dir_x          
        self.dir_y = dir_y          

    def update(self, width, height):
     if self.active:
       self.x += self.dir_x * self.speed
       self.y += self.dir_y * self.speed
     if (
        self.x < 0
        or self.x > width - self.size
        or self.y < 0
        or self.y > height - self.size
        ):
        self.active = False


    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))