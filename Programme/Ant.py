import sys
from Animal import Animal


class Ant(Animal):
    home = None
    age = list()
    role = None

    def __init__(self, element, maxlife, size, damage, maxhunger, maxthirst, anthill, lifespan):
        Animal.__init__(self, element, maxlife, size, damage, maxhunger, maxthirst)
        self.home = anthill

        self.age = list()
        self.age.append(0)
        self.age.append(lifespan)

    def alive(self):

        if self.life[0] <= 0: return False

        if self.hunger[0] > 0:
            self.hunger[0] -= 1
        else:
            return False

        if self.thirst[0] > 0:
            self.thirst[0] -= 1
        else:
            return False

        if self.age[0] < self.age[1]:
            self.age[0] += 1
        else:
            return False

        return True

    def is_alive(self):
        return self.life[0] > 0 and self.hunger[0] > 0 and self.thirst[0] > 0 and self.age[0] < self.age[1]

    def receive_damage(self, damage):
        self.life[0] -= damage

        if self.life[0] <= 0:
            self.emit_pheromone(0, 0.3)
        else:
            self.emit_pheromone(0, 0.15)

    def move_to_element(self, element):
        pass

    def action(self):
        pass

    def find_home_entrance(self):
        mini = sys.float_info.max
        element = None
        for i in self.home.entrance:
            temp = self.element.distance(i)
            if temp < mini:
                mini = temp
                element = i

        return element

    def emit_pheromone(self, p, quantity):
        self.element.get_pheromone().add_pheromone(p, quantity)

    def has_space(self):
        return self.need_refill(0.90)

    def need_rest(self):
        return self.need_refill(0.25)

    def need_refill(self, coef):
        if self.hunger[0] < self.hunger[1] * coef:
            return -1
        if self.hunger[0] < self.thirst[1] * coef:
            return 1
        return 0

    def eat_base(self):
        if self.hunger[0] < self.hunger[1] * 0.9:
            eat = 0
            if self.home.storage[0] > 10:
                eat = 10
                self.home.storage[0] -= 10
            else:
                eat = self.home.storage[0]
                self.home.storage[0] = 0
            self.hunger[0] += eat

    def drink_base(self):
        if self.thirst[0] < self.thirst[1] * 0.9:
            drink = 0
            if self.home.storage[0] > 10:
                drink = 10
                self.home.storage[0] -= 10
            else:
                drink = self.home.storage[0]
                self.home.storage[0] = 0
            self.thirst[0] += drink
            return True
        return False

    def is_ant(self):
        return True

    def post(self):
        pass
