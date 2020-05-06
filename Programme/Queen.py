from Programme.Ant import Ant
from Programme.Role import Role
<<<<<<< HEAD
from Programme.Egg import Egg
=======
>>>>>>> f7b05eea38c93b6a9724657e157c75a8741935f5


class Queen(Ant):
    lay_rate = None

    def __init__(self, anthill, element):
        Ant.__init__(self, element, 10, 4, 1, 30, 30, anthill, 1000)
        self.lay_rate = 20
        self.role = Role.PASSIVE

    def move_to_element(self, element):
        return False

    def action(self):

        if self.age[0] % self.lay_rate == 0:
            self.lay_egg()
            return True

        elif self.has_space() != 0:
            return self.consume_base()

        return False

    def lay_egg(self):
        self.home.colony.append(Egg(self.home, self.element))

    def post(self):

        self.element.post()
        print("Queen ant from the colony ", self.home.name)

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
