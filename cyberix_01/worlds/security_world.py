from worlds.world_factory import WorldFactory

from factories.monsters.security_factory import SecurityFactory

from model.bullet import Bullet
from model.clue import Clue
from components.background import Background


class SecurityWorld(WorldFactory):

    def create_monster(self, monster_type, x, y, size, speed_x, speed_y):

        if monster_type == "security":
            return SecurityFactory().create(
                x, y, size, speed_x, speed_y
            )

        else:
            raise ValueError("Unknown monster type")

    def create_bullet(self, size, speed, damage=1):
        return Bullet(size, speed, damage)

    def create_clue(self, x, y, name, description, clue_type):
        return Clue(x, y, name, description, clue_type)

    def create_background(self, width, height):
        return Background(width, height, "security_room.png")