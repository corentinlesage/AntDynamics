from Programme.Ant import Ant
from Programme.Role import Role
from Programme.Egg import Egg


class Queen(Ant):
    """
    Queen is an Ant
    It periodically lay eggs over a turn period

    lay_rate : positive integer
    role is not used and by default is put on Passive
    """
    lay_rate = None

    def __init__(self, anthill, element):
        """
        Constructor
        """
        Ant.__init__(self, element, 10, 4, 1, 30, 30, anthill, 1000)

        self.lay_rate = 15
        self.role = Role.PASSIVE

    def move_to_element(self, element):
        """
        Queen doesnt move away from Anthill
        Doesn't have a IA for movement
        """
        return False

    def action(self):
        """
        Queen will periodically lay eggs and eat and drink in the Anthill

        Return True if an action was successful
        else False
        """
        if not self.is_alive():
            self.convert_to_food()
            return False

        if self.age[0] % self.lay_rate == 0:
            self.lay_egg()
            return True

        elif self.has_space() != 0:
            return self.consume_base()

        return False

    def lay_egg(self):
        Egg(self.home, self.element)

    def post(self):
        """
        Print of a Queen
        """
        self.element.post()
        print("Queen ant from the colony ", self.home.name)

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
