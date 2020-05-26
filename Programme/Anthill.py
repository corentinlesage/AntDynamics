from Programme.Queen import Queen
from Programme.Soldier import Soldier
from Programme.Worker import Worker


class Anthill:
    """
    Anthill is a place where Ant of the same colony gather together
    it has a name, entrances composed of Element
    a list of ant belonging to the colony and a list of Ant physically in the colony
    it has a storage where food and water is store

    name : string
    entrance : list of Element where Ant enter the Anthill
    list_ant_at_home : List of Ant at the Anthill
    colony : list of Ant belonging to the Anthill
    storage : List of two positive integer
    1. food
    2. water
    """
    name = None
    entrance = list()
    list_ant_at_home = list()
    colony = list()
    storage = list()

    def __init__(self, name, entrance):
        """
        Constructor
        By default, Anthill only contains a Queen at the beginning
        Start with 100 food and 100 water
        """
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
        """
        consumption of the storage by an Ant depending of the type of store

        type : number 0 or 1, food or water
        """
        if self.storage[type] == 0:
            return 0

        elif self.storage[type] >= 10:
            self.storage[type] -= 10
            return 10

        temp = self.storage[type]
        self.storage[type] = 0
        return temp

    def post(self):
        """
        Print of an Anthill
        """

        print("Anthill:  ", self.name)

        print("Entrances: ", len(self.entrance))
        print("Ants: ", len(self.colony))
        print("Ants at home: ", len(self.list_ant_at_home))
        print("Supply: ")
        print("Food: ", self.storage[0], "Water: ", self.storage[1])
