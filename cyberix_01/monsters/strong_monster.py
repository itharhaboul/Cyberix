from monster import Monster
from monster import Monster
from damage.rules import ResistantDamage        

class StrongMonster(Monster):
     def __init__(self, x, y, size, speed_x, speed_y):
        super().__init__(x, y, size, speed_x, speed_y, damage_rule=ResistantDamage())    
        self.max_health = 4
        self.health = 4

