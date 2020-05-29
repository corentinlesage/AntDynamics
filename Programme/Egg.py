import random
from Programme.Ant import Ant
from Programme.Role import Role
from Programme.Soldier import Soldier
from Programme.Worker import Worker


class Egg(Ant):
    """
    Egg is an Ant
    It eat and drink until it hatches into a proper Ant: Soldier or Worker

    hatch: positive integer
    role is not used and by default is put on Passive
    """
    hatch = None

    def __init__(self, anthill, element):
        """
        Constructor
        """
        Ant.__init__(self, element, 10, 1, 0, 50, 50, anthill, 20)

        self.role = Role.PASSIVE
        self.hatch = 10

    def move_to_element(self, element):
        """
        Here an Egg doesnt move away from Anthill
        Doesn't have a IA for movement
        """
        return False

    def action(self):
        """
        Egg will periodically eat and drink in the Anthill
        Until it grows enough to hatch

        Return True if an action was successful
        else False
        """
        if not self.is_alive():
            self.convert_to_food()
            return False

        if self.age[0] % self.hatch == 0:
            self.hatches()
            return True

        elif self.has_space() != 0:
            return self.consume_base()

        return False

    def hatches(self):
        """
        Convert an Egg into another Ant : Soldier or Worker
        """
        temp = random.random()
        if temp < 0.3:
            Soldier(self.home, self.element)
        else:
            Worker(self.home, self.element, 10)

        self.__delete__()

    def post(self):
        """
        Print of an Egg
        """
        self.element.post()
        print("egg ant from the colony ", self.home.name)

        if self.is_alive():
            print("id: ", self.id)
            print("size: ", self.size)
            print("State: ", self.role)
            print("Life: ", self.life[0], "out of", self.life[1])
            print("Hunger: ", self.hunger[0], "out of", self.hunger[1])
            print("Thirst: ", self.thirst[0], "out of", self.thirst[1])
            print("Age: ", self.age[0], "out of", self.age[1])
            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else:
            print("is dead")
