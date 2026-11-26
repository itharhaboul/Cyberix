class LevelDirector:

    def __init__(self, builder):
        self.builder = builder

    def construct_level(self):

        self.builder.build_background()
        self.builder.build_monsters()
        self.builder.build_clues()

        return self.builder.get_level()