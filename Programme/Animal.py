from abc import ABC, abstractmethod
from random import random


class Animal(ABC):
    element = None
    life = list()
    size = None
    damage = None
    hunger = list()
    thirst = list()

    def __init__(self, element, life, size, damage, hunger, thirst):
        self.element = element
        self.life.append(life)
        self.life.append(life)
        self.size = size
        self.damage = damage
        self.hunger.append(0)
        self.hunger.append(hunger)
        self.thirst.append(0)
        self.thirst.append(thirst)

    def death(self):
        pass

    def receive_damage(self, damage):
        self.life[0] -= damage

        if self.life[0] < 0:
            self.death()

    def chose_path(self):
        list_path = self.element.get_path()

        while True:
            list_int = list()
            for i in list_path:
                temp = random.randit(0, len(list_path) - 1)
                if not list_int.__contains__(temp):
                    list_int.__add__(temp)
                if self.move_to_path(list_path[temp]):
                    return True
        return False

    def move_to_path(self, path):
        if path.get_start() == self.element:
            return self.move_to_element(path.get_end())
        return self.move_to_element(path.get_start())

    def move_to_element(self, element):
        pass

    def get_size(self):
        return self.size

    def is_ant(self):
        return False
