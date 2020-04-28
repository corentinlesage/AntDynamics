from abc import ABC, abstractmethod
import random


class Animal(ABC):
    element = None
    life = list()
    size = None
    damage = None
    hunger = list()
    thirst = list()
    is_travelling = None

    def __init__(self, element, life, size, damage, hunger, thirst):
        self.element = element
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


    def receive_damage(self, damage):
        self.life[0] -= damage

    def attack(self, enemy):
        enemy.receive_damage(self.damage)

    def alive(self):

        if self.life[0] <= 0: return False

        if self.hunger[0] > 0:
            self.hunger[0] -= 1
        else: return False

        if self.thirst[0] > 0:
            self.thirst[0] -= 1
        else: return False

        return True

    def is_alive(self):
        return self.life[0] > 0 and self.hunger[0] > 0 and self.thirst[0] > 0

    def chose_path(self):
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
        if path.get_start() == self.element:
            if self.move_to_element(path.get_end()):
                self.element.list_animal.remove(self)
                self.element = path.get_end()
                self.element.list_animal.append(self)
                self.is_travelling = path.cost
                return True
        elif self.move_to_element(path.get_start()):
            self.element.list_animal.remove(self)
            self.element = path.get_start()
            self.element.list_animal.append(self)
            self.is_travelling = path.cost
            return True
        return False

    def move_to_element(self, element):
        pass

    def travelling(self):
        if self.is_travelling > 0:
            self.is_travelling -=1
            return True
        return False

    def decomposition(self):
        self.size -= 0.01

        if self.size <= 0:
            return True
        else:
            return False

    def eat(self, food):

        if food.size > 0.1:
            food.size -= 0.1
            self.hunger += 10

        else :
            self.hunger += food.size *10
            self.element.list_animal.remove(food)
            del food

    def get_size(self):
        return self.size

    def is_ant(self):
        return False

    def action(self):
        pass

    def post(self):
        pass
