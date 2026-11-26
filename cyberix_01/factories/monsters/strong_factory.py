from monsters.strong_monster import StrongMonster
from factories.monsters.monster_factory import MonsterFactory


class StrongFactory(MonsterFactory):

    def create(self, x, y, size, speed_x, speed_y):
        return StrongMonster(x, y, size, speed_x, speed_y)