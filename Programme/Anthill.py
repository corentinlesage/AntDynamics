import Element
import Ant
from Queen import Queen
from Soldier import Soldier


class Anthill:
    name = None
    entrance = list()
    colony = list()
    storage = list()

    def __init__(self, name, entrance):
        self.name = name

        self.entrance = list()
        self.entrance = entrance

        self.colony = list()
        # self.colony.append(Queen(self, entrance[0]))
        self.colony.append(Soldier(self, entrance[0]))

        self.storage = list()
        self.storage.append(0)
        self.storage.append(0)

        for c in self.colony:
            self.add_animal(entrance[0], c)

    def add_animal(self, entrance, animal):
        if not animal.is_ant():
            temp = animal.get_size()
            if temp > entrance.capacity[1] - entrance.capacity[0]:
                return False
            entrance.capacity[0] += temp

        entrance.list_animal.append(animal)

        return True

    def refill(self, type):

        if self.storage[type] == 0:
            return 0

        elif self.storage[type] >= 10:
            self.storage[type] -= 10
            return 10

        temp = self.storage[type]
        self.storage[type] = 0
        return temp
