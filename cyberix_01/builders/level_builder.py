from abc import ABC, abstractmethod


class LevelBuilder(ABC):

    @abstractmethod
    def build_background(self):
        pass

    @abstractmethod
    def build_monsters(self):
        pass

    @abstractmethod
    def build_clues(self):
        pass

    @abstractmethod
    def get_level(self):
        pass