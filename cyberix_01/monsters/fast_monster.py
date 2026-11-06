from monster import Monster
class FastMonster(Monster):

    def __init__(self, x, y, size, speed_x, speed_y):
        super().__init__(x, y, size, speed_x, speed_y)

        self.speed_x *= 2
        self.speed_y *= 2