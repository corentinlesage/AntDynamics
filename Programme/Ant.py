from abc import ABC, abstractmethod
from Animal import Animal


class Ant(Animal):
    home = None
    age = []

    def __init__(self, element, maxlife, size, damage, maxhunger, maxthirst, anthill, lifespan):
        super(Animal, self).__init__(self, element, maxlife, size, damage, maxhunger, maxthirst)
        self.home = anthill
        self.age.append(0)
        self.age.append(lifespan)