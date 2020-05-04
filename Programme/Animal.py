from abc import ABC, abstractmethod
import random



from Programme.Supply import Supply


class Animal(ABC):
    element = None
    path = None
    life = list()
    size = None
    damage = None
    hunger = list()
    thirst = list()
    is_travelling = None

    def __init__(self, element, life, size, damage, hunger, thirst):
        self.element = element
        self .path = None
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

    def __delete__(self):

        if self.is_ant() and self.home.entrance.contains(self.element):
            pass
        else:
            self.element.capacity -= self.size

        self.element.list_animal.remove(self)

        if self.path is not None:
            self.path.capacity[0] -= self.size

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
        if path.capacity[0] + self.size <= path.capacity[1]:
            if path.get_start() == self.element:
                if path.get_end().capacity[0] + self.size <= path.get_end().capacity[1]:

                    if self.move_to_element(path.get_end()):

                        if path.get_end().add_animal(self):
                            self.element.remove_animal(self)
                            self.element = path.get_end()

                            self.is_travelling = path.cost
                            self.path = path
                            path.capacity[0] += self.size
                            return True

        return False

    def move_to_element(self, element):
        pass

    def travelling(self):
        if  self.is_travelling > 0:
            self.is_travelling -= 1
            return True

        if self.path is not None:
            self.path.capacity[0] -= self.size
            self.path = None
        return False

    def convert_to_food(self):

        self.element.list_supply.append(Supply(self.element, self.size*10, 1))

        del self

    def consume(self, supply):

        temp = 0

        if supply.quantity > 10:
            supply.quantity -= 10
            temp = 10

        else:
            temp = supply.quantity
            del supply

        if supply.type == -1:
            self.thirst[0] += temp
        elif supply.type == 1:
            self.hunger[0] += temp

    def get_size(self):
        return self.size

    def is_ant(self):
        return False

    def action(self):
        pass

    def post(self):
        pass
