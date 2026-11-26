from monsters.flying_monster import FlyingMonster
from factories.monsters.monster_factory import MonsterFactory


class FlyingFactory(MonsterFactory):

    def create(self, x, y, size, speed_x, speed_y):
        return FlyingMonster(x, y, size, speed_x, speed_y)