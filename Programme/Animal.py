from abc import ABC, abstractmethod
import random

from Programme.Supply import Supply
from Programme.Role import Role


class Animal(ABC):
    """
    Animal regroup every entity that move on the the Environment
    his current position is signified by element
    if Animal is travelling, is travelling contains the number of turns it has to wait until it reach destination
    and path contains the Path used to travel

    the size of Animal is used to determine the capacity of Element and Path to see
    if Animal can fit in

    the id helps identify an element individually

    ID : positive integer
    id : positive integer
    element : Element
    path : Path or None
    is_travelling : positive integer

    life : list of two values
    1. actual life of Animal
    2. life max of Animal

    hunger : list of two values
    1. actual life of Animal
    2. life max of Animal

    thirst : list of two values
    1. actual thirst of Animal
    2. thirst max of Animal

    size : positive integer
    role : Role
    """
    ID = 0
    id = None
    element = None
    path = None
    life = list()
    size = None
    damage = None
    hunger = list()
    thirst = list()
    is_travelling = None
    role = None

    def __init__(self, element, life, size, damage, hunger, thirst):
        """
        Constructor
        """
        self.id = Animal.ID
        Animal.ID += 1

        self.element = element
        self.path = None
        self.life = list()
        self.life.append(life)
        self.life.append(life)
        self.size = size
        self.damage = damage

        self.hunger = list()
        self.hunger.append(hunger)
        self.hunger.append(hunger)

        self.thirst = list()
        self.thirst.append(thirst)
        self.thirst.append(thirst)

        self.is_travelling = 0

        self.role = Role.PASSIVE

        self.element.add_animal(self)

    def __delete__(self):
        """
        Destructor
        Remove Animal from the Element
        and the size or capacity he take in the Element and Path associated
        """

        if self.is_ant() and self.element in self.home.entrance:
            pass
        else:
            self.element.capacity[0] -= self.size

        self.element.list_animal.remove(self)

        if self.path is not None:
            self.path.capacity[0] = self.path.capacity[0] - self.size

    def receive_damage(self, damage):
        """
        Reduce life according to the damage given

        damage : positive integer
        """
        self.life[0] -= damage

        if self.is_ant():
            if self.role != Role.Search or self.role == Role.REST:
                self.role = Role.FLEE

    def attack(self, enemy):
        """
        Attack an enemy

        enemy : Animal
        """
        enemy.receive_damage(self.damage)

    def heal(self):
        """
        Heal naturally depending of the hunger and thirst level and the size of the Animal
        """

        if self.life[0] < self.life[1]:
            self.life[0] += (self.hunger[0] / self.hunger[1] + self.thirst[0] / self.thirst[1]) * self.size

            if self.life[0] > self.life[1]:
                self.life[0] = self.life[1]

    def alive(self):
        """
        State if Animal is still alive by checking and update his stats

        Return True if the conditions are met
        else False
        """
        if self.life[0] <= 0:
            return False

        self.heal()

        if self.hunger[0] > 0:
            self.hunger[0] -= 0.1
        else:
            return False

        if self.thirst[0] > 0:
            self.thirst[0] -= 0.1
        else:
            return False

        return True

    def is_alive(self):
        """
        Check if Animal is alive without updating its stats
        """
        return self.life[0] > 0 and self.hunger[0] > 0 and self.thirst[0] > 0

    def has_space(self):
        """
        Check survival stats for a 10 space gap
        """
        return self.need_refill(10)

    def need_rest(self):
        """
        Check survival stats for a 80 space gap
        """
        return self.need_refill(80)

    def need_refill(self, coef):
        """
        Check survival stats depending of a coef given

        coef : positive integer
        Return -1 if it needs Water
        1 if it needs Food
        else 0
        """
        if self.hunger[0] < self.hunger[1] - coef:
            return 1
        if self.thirst[0] < self.thirst[1] - coef:
            return -1
        return 0

    def chose_path(self):
        """
        Choose randomly a Path to move to another Element

        Return True if the Path is valid
        else False
        """
        list_path = self.element.list_path

        while True:
            list_int = list()
            for i in list_path:
                temp = random.randint(0, len(list_path) - 1)

                if not list_int.__contains__(temp):
                    list_int.append(temp)
                    if self.move_to_path(list_path[temp]):
                        return True
        return False

    def move_to_path(self, path):
        """
        Check if a Path is valid depending of his max capacity
        Remove Animal from its previous Element and place it in his new one

        path : Path
        Return True if the Path is valid
        else False
        """
        if path.capacity[0] + self.size <= path.capacity[1]:
            if path.get_start() == self.element:
                if path.get_end().capacity[0] + self.size <= path.get_end().capacity[1]:

                    if self.move_to_element(path.get_end()):

                        if path.get_end().add_animal(self):
                            self.element.remove_animal(self)
                            self.element = path.get_end()

                            self.is_travelling = path.cost - 1
                            self.path = path
                            path.capacity[0] += self.size
                            return True

        return False

    def move_to_element(self, element):
        """
        Depending of the Animal IA choose if the Element is a valid travel

        element : Element
        Return True if the Element is valid
        else False
        """
        pass

    def travelling(self):
        """
        Reduce the travelling process by one if the Animal is travelling

        Return True if Animal is still travelling
        else False
        """
        if self.is_travelling > 0:
            self.is_travelling -= 1
            return True

        if self.path is not None:
            self.path.capacity[0] -= self.size
            self.path = None
        return False

    def convert_to_food(self):
        """
        Convert an Animal to food when it dies depending of it size
        then delete it
        """
        self.element.list_supply.append(Supply(self.element, self.size * 10, 1))

        self.__delete__()

    def consume(self, supply):
        """
        Consume a portion of the Supply

        supply : Supply
        """
        temp = 0

        if supply.quantity > 10:
            supply.quantity -= 10
            temp = 10

        else:
            temp = supply.quantity
            del supply

        if type == -1:
            self.thirst[0] += temp
        elif type == 1:
            self.hunger[0] += temp

    def get_size(self):
        return self.size

    def is_ant(self):
        return False

    def is_predator(self):
        return False

    def action(self):
        """
        Depending of the Animal IA interact on the Element
        When an Animal dies it will be converted to food
        """
        pass

    def post(self):
        """
        Print of an Animal
        """
        pass
