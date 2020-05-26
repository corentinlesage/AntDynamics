from Programme.Position import Position
from Programme.Pheromone import Pheromone


class Element:
    """
    Element is a place in the environment were Event occur
    and Animal interact with Animal and Supply
    Ant can also interact with Pheromone

    the id helps identify an element individually
    it has a radius for it size, a position in space and a maximum capacity of Animal

    ID : positive integer
    id : positive integer
    radius : positive real number
    capacity : list of two values
    1. actual capacity of Element
    2. capacity max of Element

    position : Position
    pheromone : Pheromone
    list_animal : list of Animal
    list_path : list of Path
    list_supply : List of Supply
    """
    ID = 0
    id = None
    radius = None
    capacity = list()

    position = None
    pheromone = None
    list_animal = list()
    list_path = list()
    list_supply = list()

    def __init__(self, radius, capacity, x, y):
        """
        Constructor
        """
        self.id = Element.ID
        Element.ID += 1

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
        """
        add an existing path to element
        path : Path
        """
        self.list_path.append(path)

    def remove_animal(self, animal):
        """
        Remove an animal from the element
        if the element is an anthill entrance, remove the animal from the anthill location
        Reduce the size taken by the animal in the element
        animal : Animal
        """

        if not animal.is_ant():
            self.capacity[0] -= animal.get_size()
        else:
            if animal in animal.home.list_ant_at_home:
                animal.remove_from_home()

        self.list_animal.remove(animal)

    def add_animal(self, animal):
        """
        Add an animal from the element
        if the element is an anthill entrance, add the animal from the anthill location
        Increase the size taken by the animal in the element
        animal : Animal
        return True if the add was succesfull
        else False : not enough space in the element
        """
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
        """
        add an existing supply to element
        supply : Supply
        """
        self.list_supply.append(supply)

    def get_path(self):
        return self.list_path

    def get_pheromone(self):
        return self.pheromone

    def is_supply(self):
        """
        Return the supply if a supply exist in the element
        else None
        """
        for i in self.list_supply:
            return i

        return None

    def is_enemy(self, anthill):
        """
        Return the animal if an animal that is not from the same anthill exist in the element
        else None
        anthill : Anthill
        """
        for i in self.list_animal:
            if i.is_ant():
                if i.home != anthill:
                    return i
            else:
                return i
        return None

    def is_not_predator(self):
        """
        Return the animal if an animal that is not a predator exist in the element
        else None
        """
        for i in self.list_animal:
            if not i.is_predator():
                return i
        return None

    def distance(self, element):
        """
        Return the distance value, positive real number from another element
        """
        return self.position.distance(element.position)

    def post(self):
        """
        Print of the element
        """
        print("\nelement:")
        print("id: ", self.id)
        self.position.post()
        self.pheromone.post()

        print("nombre d'animaux: ", len(self.list_animal))
        print("nombre de tas: ", len(self.list_supply))

        temp = 0
        for i in self.list_path:
            temp += i.capacity[0]

        print("taille total d'animaux en trajets: ", temp)
