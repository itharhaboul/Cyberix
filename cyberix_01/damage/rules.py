from damage.damage_rule import DamageRule

class NormalDamage(DamageRule):
    def compute(self, weapon):
        return weapon.damage       # retourne les dégâts de l'arme

class ResistantDamage(DamageRule): #concernnat strong montser
    def compute(self, weapon):
        return weapon.damage * 0.75     # il prend la moitié des dégâts

class WeaknessDamage(DamageRule): # pour le flying monsterr
    def compute(self, weapon):
        return weapon.damage * 2        # il prend le double