from damage.rules import NormalDamage


class Monster:

    def __init__(self, x, y, size, speed_x, speed_y, damage_rule=None):

        self.x = x
        self.y = y

        self.start_x = x
        self.start_y = y

        self.size = size

        self.speed_x = speed_x
        self.speed_y = speed_y

        self.max_health = 3
        self.health = 3

        self.damage_rule = (
            damage_rule if damage_rule is not None else NormalDamage()
        )

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def update(self, width, height):

        self.move()

        if self.x > width - self.size or self.x < 0:
            self.speed_x = -self.speed_x

        if self.y > height - self.size or self.y < 0:
            self.speed_y = -self.speed_y

    def hit(self, weapon):

        damage = self.damage_rule.compute(weapon)
        self.health = self.health - damage

    def respawn(self):

        self.x = self.start_x
        self.y = self.start_y
        self.health = self.max_health