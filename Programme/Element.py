<<<<<<< HEAD
from Programme.Position import Position
from Programme.Pheromone import Pheromone
=======
from Path import Path
from Programme.Position import Position
from Programme.Pheromone import Pheromone
from Animal import Animal
>>>>>>> f7b05eea38c93b6a9724657e157c75a8741935f5


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

        if not animal.is_ant():
            self.capacity[0] -= animal.get_size()
        else:
            if animal in animal.home.list_ant_at_home:
                animal.remove_from_home()

        self.list_animal.remove(animal)

    def add_animal(self, animal):

        if not animal.is_ant():
            temp = animal.get_size()
            if temp > self.capacity[1] - self.capacity[0]:
                return False
            self.capacity[0] += temp

        elif animal in animal.home.list_ant_at_home:
            animal.add_from_home()

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

        print("nombre d'animaux: ", len(self.list_animal))
        print("nombre de tas: ", len(self.list_supply))

        temp = 0
        for i in self.list_path:
            temp += i.capacity[0]

        print("taille total d'animaux en trajets: ", temp)
