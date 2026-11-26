from monsters.fast_monster import FastMonster
from factories.monsters.monster_factory import MonsterFactory


class FastFactory(MonsterFactory):

    def create(self, x, y, size, speed_x, speed_y):
        return FastMonster(x, y, size, speed_x, speed_y)