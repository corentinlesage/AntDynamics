import Element
import Ant
from Queen import Queen
from Programme.Soldier import Soldier
from Programme.Worker import Worker


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
        self.colony.append(Worker(self, entrance[0], 10))

        self.storage = list()
        self.storage.append(0)
        self.storage.append(0)

        for c in self.colony:
            entrance[0].add_animal(c)

    def refill(self, type):

        if self.storage[type] == 0:
            return 0

        elif self.storage[type] >= 10:
            self.storage[type] -= 10
            return 10

        temp = self.storage[type]
        self.storage[type] = 0
        return temp

    def post(self):

        print("Anthill:  ", self.name)


        print("Entrances: ", len(self.entrance))
        print("Ants: ", len(self.colony))
        print("Supply: ")
        print("Food: ", self.storage[0], "Water: ", self.storage[1])