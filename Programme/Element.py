from Path import Path
from Position import Position
from Pheromone import Pheromone
from Animal import Animal


class Element:
    radius = None
    capacity = list()

    position = None
    pheromone = None
    list_animal = list()
    list_path = list()
    list_supply = list()

    def __init__(self, radius, capacity, x, y):
        self.radius = radius

        self.capacity = list()
        self.capacity.append(0)
        self.capacity.append(capacity)
        self.position = Position(x, y)
        self.pheromone = Pheromone(0, 0, 0)

        self.list_animal = list()
        self.list_path = list()

        self.list_supply = list()

    def add_path(self, path):
        self.list_path.append(path)

    def remove_animal(self, animal):
        if not animal.is_ant() and animal.home.entrance.contains(self):
            self.capacity[0] -= animal.get_size()

        self.list_animal.remove(animal)

    def add_animal(self, animal):
        if not animal.is_ant() and animal.home.entrance.contains(self):
            temp = animal.get_size()
            if temp > self.capacity[1] - self.capacity[0]:
                return False
            self.capacity[0] += temp

        self.list_animal.append(animal)

        return True

    def add_supply(self, supply):
        self.list_supply.append(supply)

    def get_path(self):
        return self.list_path

    def get_pheromone(self):
        return self.pheromone

    def is_supply(self):
        for i in self.list_supply:
                return i

        return None

    def is_enemy(self, anthill):
        for i in self.list_animal:
            if i.is_ant():
                if i.home != anthill:
                    return i
            else:
                return i
        return None

    def distance(self, element):
        return self.position.distance(element.position)

    def post(self):
        print("\nelement:")
        self.position.post()
        self.pheromone.post()
