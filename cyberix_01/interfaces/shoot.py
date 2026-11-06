from abc import ABC, abstractmethod

class Shootable(ABC):

    @abstractmethod
    def shoot(self, bullet, target_x, target_y):
        pass