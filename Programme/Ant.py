import sys
from Programme.Animal import Animal


class Ant(Animal):
    """
    Ant is an Animal

    home : Anthill
    age : list of 2 positives integers
    1. actual age
    2. max age
    """
    home = None
    age = list()

    def __init__(self, element, maxlife, size, damage, maxhunger, maxthirst, anthill, lifespan):
        """
        Constructor
        """
        self.home = anthill
        Animal.__init__(self, element, maxlife, size, damage, maxhunger, maxthirst)

        self.age = list()
        self.age.append(0)
        self.age.append(lifespan)

        anthill.list_ant_at_home.append(self)

    def __delete__(self):
        """
        Destructor

        Remove Ant from its Anthill
        """
        self.home.colony.remove(self)
        self.home.list_ant_at_home.remove(self)

        super().__delete__()

    def alive(self):
        """
        As Animal, verify if Ant is still alive with age
        update the values

        Return True if the conditions are met
        else False
        """
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
        """
        Check if Animal is alive without updating its stats and with age
        """
        return self.life[0] > 0 and self.hunger[0] > 0 and self.thirst[0] > 0 and self.age[0] < self.age[1]

    def receive_damage(self, damage):
        """
        Receive damage by emiting the danger pheromone
        """
        self.life[0] -= damage

        if self.life[0] <= 0:
            self.emit_pheromone(0, 0.3)
        else:
            self.emit_pheromone(0, 0.15)

    def move_to_element(self, element, path):
        """
        Depending of the Ant IA choose if the Element is a valid travel

        element : Element
        Return True if the Element is valid
        else False
        """
        pass

    def action(self):
        """
        Depending of the Ant IA interact on the Element
        """
        pass

    def find_home_entrance(self):
        """
        Allow an Ant to find the closest Path to his Anthill by returning the closest Element to it

        Return : Element
        """
        mini = sys.float_info.max
        element = None
        for i in self.home.entrance:
            temp = self.element.distance(i)
            if temp < mini:
                mini = temp
                element = i

        return element

    def emit_pheromone(self, p, quantity):
        """
        Allow an Ant to emit pheromone depending of its type p and quantity

        p : number 0, 1 or 2
        quantity : real number between 0 and 1
        """
        self.element.get_pheromone().add_pheromone(p, quantity)

    def consume_base(self):
        """
        Allow an Ant to eat and drink directly in his Anthill storage
        return True if the action succeeded
        else False
        """
        ind = -1

        if self.hunger[0] < self.hunger[1] - 10:
            ind = 0
        elif self.thirst[0] < self.thirst[1] - 10:
            ind = 1

        if self.home.storage[ind] > 10:
            eat = 10
            self.home.storage[ind] -= 10
        else:
            eat = self.home.storage[ind]
            self.home.storage[ind] = 0

        if ind == 0:
            self.hunger[0] += eat
            return True
        else:
            self.thirst[0] += eat
            return True

        return False

    def is_ant(self):
        return True

    def post(self):
        """
        Print of an Ant
        """
        pass

    def remove_from_home(self):
        self.home.list_ant_at_home.remove(self)

    def add_from_home(self):
        self.home.list_ant_at_home.append(self)
