import random
from Programme.Ant import Ant
from Programme.Role import Role
from Programme.Soldier import Soldier
from Programme.Worker import Worker


class Egg(Ant):
    hatch = None

    def __init__(self, anthill, element):
        Ant.__init__(self, element, 10, 1, 0, 50, 50, anthill, 20)

        self.role = Role.PASSIVE
        self.hatch = 15

    def move_to_element(self, element):
        return False

    def action(self):

        if self.age[0] % self.hatch == 0:
            self.hatches()
            return True

        elif self.has_space() != 0:
            return self.consume_base()

        return False

    def hatches(self):

        temp = random.random()
        if temp < 0.3:
            self.home.colony.append(Soldier(self.home, self.element))
        else:
            self.home.colony.append(Worker(self.home, self.element, 10))

        self.__delete__()

    def post(self):

        self.element.post()
        print("egg ant from the colony ", self.home.name)

        if self.is_alive():
            print("size: ", self.size)
            print("State: ", self.role)
            print("Life: ", self.life[0], "out of", self.life[1])
            print("Hunger: ", self.hunger[0], "out of", self.hunger[1])
            print("Thirst: ", self.thirst[0], "out of", self.thirst[1])
            print("Age: ", self.age[0], "out of", self.age[1])
            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else:
            print("is dead")
