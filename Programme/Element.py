from Path import Path
from Position import Position
from Pheromone import Pheromone
from Animal import Animal


class Element:
    radius = None
    capacity = list()

    position = None
    pheromone = None
    listAnimal = list()
    listPath = list()

    def __init__(self, radius, capacity, x, y):
        self.radius = radius
        self.capacity.append(0)
        self.capacity.append(capacity)
        self.position = Position(x, y)
        self.pheromone = Pheromone(0, 0, 0)

    def add_path(self, path):
        self.listPath.append(path)
