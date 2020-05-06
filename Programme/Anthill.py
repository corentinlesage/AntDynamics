<<<<<<< HEAD
from Programme.Queen import Queen
=======
import Element
import Ant
from Queen import Queen
>>>>>>> f7b05eea38c93b6a9724657e157c75a8741935f5
from Programme.Soldier import Soldier
from Programme.Worker import Worker


class Anthill:
    name = None
    entrance = list()
    list_ant_at_home = list()
    colony = list()
    storage = list()

    def __init__(self, name, entrance):
        self.name = name

        self.list_ant_at_home = list()

        self.entrance = list()
        self.entrance = entrance

        self.colony = list()
        self.colony.append(Queen(self, entrance[0]))
        # self.colony.append(Soldier(self, entrance[0]))
        # self.colony.append(Worker(self, entrance[0], 10))

        self.storage = list()
        self.storage.append(100)
        self.storage.append(100)

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
        print("Ants at home: ", len(self.list_ant_at_home))
        print("Supply: ")
        print("Food: ", self.storage[0], "Water: ", self.storage[1])
