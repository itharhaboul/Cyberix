from abc import ABC, abstractmethod

class DamageRule(ABC): #toute règle de dégâts doit avoir compute
    @abstractmethod
    def compute(self, weapon):
        pass     