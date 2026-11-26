from abc import ABC, abstractmethod


class MonsterFactory(ABC):

    @abstractmethod
    def create(self, x, y, size, speed_x, speed_y):
        pass