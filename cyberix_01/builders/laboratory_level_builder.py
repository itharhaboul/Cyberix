from builders.level_builder import LevelBuilder
from model.level import Level
from worlds.laboratory_world import LaboratoryWorld


class LaboratoryLevelBuilder(LevelBuilder):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.factory = LaboratoryWorld()
        self.level = None

    def build_background(self):
        background = self.factory.create_background(
            self.width, self.height
        )

        self.level = Level(background)

    def build_monsters(self):
        normal = self.factory.create_monster(
            "normal", 100, 100, 50, 3, 2
        )

        fast = self.factory.create_monster(
            "fast", 300, 200, 50, 4, 2
        )

        self.level.monsters.extend([normal, fast])

    def build_clues(self):

        clues = [
            (
                150, 150,
                "Computer Terminal",
                "The computer shows that the robots were built to work alone",
                "computer"
            ),
            (
                650, 150,
                "Robot Part",
                "This broken part belongs to one of the laboratory robots..",
                "robot_part"
            ),
            (
                650, 450,
                "Research Document",
                "The final report mentions an unauthorized experiment in the Security Room.",
                "document"
            )
        ]

        for x, y, name, description, clue_type in clues:

            clue = self.factory.create_clue(
                x, y, name, description, clue_type
            )

            self.level.clues.append(clue)

    def get_level(self):
        return self.level