import pygame
from player import Player
from monster import Monster
from bullet import Bullet

def overlaps(ax, ay, a_size, bx, by, b_size):      # to control if bullets touch the monster(it depends abouht health,scors..)
    return (ax < bx + b_size and ax + a_size > bx
            and ay < by + b_size and ay + a_size > by)

class GameBoard:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CyberiX")
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.font = pygame.font.Font(None, 30)

# create objects from  classes
        self.player = Player(400, 300, 50, 5)
        self.monster = Monster(100, 50, 50, 3, 2)       
        self.bullet = Bullet(10, 10)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()   # etat de clavier
        self.player.handle_input(keys)
        self.player.keep_inside(self.width, self.height)

        if keys[pygame.K_SPACE] and not self.bullet.active:
            start_x = self.player.x + self.player.size // 2 - self.bullet.size // 2    
            start_y = self.player.y + self.player.size // 2 - self.bullet.size // 2    
            self.bullet.fire(start_x, start_y, self.player.dir_x, self.player.dir_y)   

        self.bullet.update(self.width, self.height)     
        self.monster.update(self.width, self.height)    
        if self.bullet.active and overlaps(self.bullet.x, self.bullet.y, self.bullet.size,    
            self.monster.x, self.monster.y, self.monster.size):
            self.bullet.active = False                  # la balle disparaît
            self.monster.hit()                          # le monstre perd 1 de vie
            if self.monster.health <= 0:                
                self.score = self.score + 1
                self.monster.respawn()

    def draw(self):
        self.screen.fill((180, 180, 180))
        self.player.draw(self.screen)
        self.monster.draw(self.screen)
        self.bullet.draw(self.screen)
        score_text = self.font.render( f"Score: {self.score}", True, (0, 0, 0) )
        self.screen.blit( score_text, (self.width - score_text.get_width() - 15, 15) )
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()