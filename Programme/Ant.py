from Animal import Animal


class Ant(Animal):
    home = None
    age = list()

    def __init__(self, element, maxlife, size, damage, maxhunger, maxthirst, anthill, lifespan):
        super(Animal, self).__init__(self, element, maxlife, size, damage, maxhunger, maxthirst)
        self.home = anthill
        self.age.append(0)
        self.age.append(lifespan)

    def move_to_element(self, element):
        pass


    def is_ant(self):
        return True
