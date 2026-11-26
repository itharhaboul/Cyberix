from defenses.security_monster import SecurityMonster
from factories.monsters.monster_factory import MonsterFactory


class SecurityFactory(MonsterFactory):

    def create(self, x, y, size, speed_x=None, speed_y=None):
        return SecurityMonster(x, y, size)