import Element
import Ant
from Queen import Queen


class Anthill:
    entrance = list()
    colony = list()

    def __init__(self, entrance):
        self.entrance = entrance
        self.colony.append(Queen(self, entrance[0]))

        for c in self.colony:
            self.addAnimal(entrance[0], c)

    def add_animal(self, entrance, animal):
        if not animal.is_ant():
            temp = animal.get_size()
            if temp > entrance.capacity[1] - entrance.capacity[0]:
                return False
            entrance.capacity[0] += temp

        entrance.list_animal.append(animal)