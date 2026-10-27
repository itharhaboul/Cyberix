import pygame
class Player:
    def __init__(self, x, y, size, speed):   # constructeur : preparer les informations du player
        self.x = x                           #  slef cest l objet actuel pour instant et chaque objet a ses propres informations
        self.y = y
        self.size = size
        self.speed = speed
        self.dir_x = 0                       # direction regardee 

    def handle_input(self, keys):            # le mouvement du player
        dx = 0
        dy = 0
        if keys[pygame.K_RIGHT]:
            dx = 1
        elif keys[pygame.K_LEFT]:
            dx = -1

        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        # Normaliser la vitesse 
        if dx != 0 and dy != 0:
            factor = 0.7071
        else:
            factor = 1

        self.x += dx * self.speed * factor
        self.y += dy * self.speed * factor

        # Garder la dernière direction
        if dx != 0 or dy != 0:
            self.dir_x = dx
            self.dir_y = dy

    def keep_inside(self, width, height):    # le player reste dans le windowz
        if self.x > width - self.size:
            self.x = width - self.size
        if self.x < 0:
            self.x = 0
        if self.y > height - self.size:
            self.y = height - self.size
        if self.y < 0:
            self.y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))
        center_x = self.x + self.size // 2 
        center_y = self.y + self.size // 2  
        end_x = center_x + self.dir_x * self.size // 2
        end_y = center_y + self.dir_y * self.size // 2
        pygame.draw.line(screen, (255, 255, 255), (center_x, center_y), (end_x, end_y), 3)