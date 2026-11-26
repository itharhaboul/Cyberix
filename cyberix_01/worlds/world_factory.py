from abc import ABC, abstractmethod


class WorldFactory(ABC):

    @abstractmethod
    def create_monster(self, *args):
        pass

    @abstractmethod
    def create_bullet(self, size, speed, damage=1):
        pass

    @abstractmethod
    def create_clue(self, x, y):
        pass

    @abstractmethod
    def create_background(self, width, height):
        pass