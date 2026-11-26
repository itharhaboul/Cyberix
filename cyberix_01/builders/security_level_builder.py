from builders.level_builder import LevelBuilder
from model.level import Level
from worlds.security_world import SecurityWorld


class SecurityLevelBuilder(LevelBuilder):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.factory = SecurityWorld()
        self.level = None

    def build_background(self):
        background = self.factory.create_background(
            self.width, self.height
        )

        self.level = Level(background)

    def build_monsters(self):
        security = self.factory.create_monster(
            "security", 700, 300, 50, 3, 2
        )

        self.level.security_monsters.append(security)

    def build_clues(self):

        clues = [
            (
                150, 150,
                "Security Access Log",
                "The access log shows that someone entered the Security Room after the experiment was officially stopped.",
                "access_log"
            ),
            (
                400, 150,
                "Security Camera",
                "The camera recording reveals that the security robot was protecting a restricted laboratory area.",
                "camera"
            ),
            (
                600, 450,
                "Encrypted File",
                "This file contains important information about the secret experiment..An access code is required to read it.",
                "encrypted_file"
            )
        ]

        for x, y, name, description, clue_type in clues:

            clue = self.factory.create_clue(
                x, y, name, description, clue_type
            )

            self.level.clues.append(clue)

    def get_level(self):
        return self.level