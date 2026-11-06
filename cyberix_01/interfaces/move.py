from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):  # any class wants to have movable interfce,must have also def move!
        pass 