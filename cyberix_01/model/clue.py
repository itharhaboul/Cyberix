class Clue:

    def __init__(self, x, y, name, description, clue_type):

        self.x = x
        self.y = y

        self.name = name
        self.description = description
        self.clue_type = clue_type

        self.collected = False