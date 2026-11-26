from model.monster import Monster
from factories.monsters.monster_factory import MonsterFactory


class NormalFactory(MonsterFactory):

    def create(self, x, y, size, speed_x, speed_y):
        return Monster(x, y, size, speed_x, speed_y)