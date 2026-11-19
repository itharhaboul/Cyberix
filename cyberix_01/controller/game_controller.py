import pygame

from model.game_model import GameModel
from view.game_view import GameView


class GameController:

    def __init__(self):

        pygame.init()

        self.width = 800
        self.height = 600

        self.model = GameModel(self.width, self.height)

        self.view = GameView(self.width, self.height)

        self.clock = pygame.time.Clock()

        self.running = True

    # Handle window events
    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    # Handle keyboard input
    def handle_input(self):

      keys = pygame.key.get_pressed()

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

      self.model.player.move(dx, dy)

      self.model.player.keep_inside(
         self.width,
         self.height
    )
 # Space = Shoot
      if keys[pygame.K_SPACE] and not self.model.bullet.active:
         self.model.shoot_player()

    # Run game
    def run(self):

        while self.running:

            self.handle_events()

            self.handle_input()

            self.model.update()

            self.view.draw(self.model)

            self.clock.tick(60)

        pygame.quit()