import pygame

from model.game_model import GameModel
from view.game_view import GameView

from builders.level_director import LevelDirector
from builders.laboratory_level_builder import LaboratoryLevelBuilder
from builders.security_level_builder import SecurityLevelBuilder


class GameController:

    def __init__(self):

        pygame.init()

        self.width = 800
        self.height = 600

        # Initialize the display
        self.view = GameView(self.width, self.height)

        # Start with Laboratory
        self.director = LevelDirector(
            LaboratoryLevelBuilder(self.width, self.height)
        )

        level = self.director.construct_level()

        # Create GameModel
        self.model = GameModel(
            self.width,
            self.height,
            level
        )

        self.current_level = "laboratory"

        self.clock = pygame.time.Clock()
        self.running = True

    # Change Level
    def change_level(self, builder, level_name):

        self.director = LevelDirector(builder)

        new_level = self.director.construct_level()

        self.model.level = new_level

        self.model.monsters = new_level.monsters
        self.model.security_monsters = new_level.security_monsters

        self.model.security = (
            self.model.security_monsters[0]
            if self.model.security_monsters
            else None
        )

        # Reset bullets
        self.model.bullet.active = False
        self.model.security_bullet.active = False

        # Reset player position
        self.model.player.x = 400
        self.model.player.y = 300

        # Reset investigation system
        self.model.collected_clues = 0
        self.model.nearby_clue = None
        self.model.active_clue = None

        self.current_level = level_name

    # Handle Events
    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            # Keyboard events
            elif event.type == pygame.KEYDOWN:

                # Close evidence information
                if event.key == pygame.K_ESCAPE:

                    if self.model.active_clue is not None:
                        self.model.close_clue()

                # Investigate nearby evidence
                elif event.key == pygame.K_e:

                    if self.model.active_clue is None:
                        self.model.interact()

    # Handle Player Input
    def handle_input(self):

        # Stop movement while reading evidence
        if self.model.active_clue is not None:
            return

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

        if keys[pygame.K_SPACE] and not self.model.bullet.active:
            self.model.shoot_player()

    # Main Game Loop
    def run(self):

        while self.running:

            self.handle_events()

            self.handle_input()

            self.model.update()

            # Check Laboratory completion
            if (
                self.current_level == "laboratory"
                and self.model.collected_clues == len(self.model.level.clues)
                and self.model.active_clue is None
            ):

                self.change_level(
                    SecurityLevelBuilder(self.width, self.height),
                    "security"
                )

            self.view.draw(self.model)

            self.clock.tick(60)

        pygame.quit()