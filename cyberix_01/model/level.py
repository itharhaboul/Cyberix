class Level:

    def __init__(self, background, door=None):
        self.background = background
        self.door = door

        self.monsters = []
        self.security_monsters = []
        self.clues = []