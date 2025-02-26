
"""It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same family.
"""
from abc import abstractmethod, ABC


class Building(ABC):
    def __init__(self):
        self.build_walls()
        self.build_floor()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_floor(self):
        pass


class HighRise(Building):
    def build_walls(self):
        print('building highrise walls')

    def build_floor(self):
        print('building highrise floor')

class Villa(Building):
    def build_walls(self):
        print('building villa walls')

    def build_floor(self):
        print('building villa floor')


if __name__ == '__main__':
    HighRise()
    Villa()
