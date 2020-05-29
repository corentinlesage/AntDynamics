from Programme.Animal import Animal
from Programme.Role import Role


class Prey(Animal):
    """
    Prey is an Animal
    it wonders the Environment for food
    """
    def __init__(self, element, life, size, damage, hunger, thirst):
        """
        Constructor
        """
        Animal.__init__(self, element, life, size, damage, hunger, thirst)

    def move_to_element(self, element):
        """
        Doesnt interact with Pheromone
        Always take the element picked
        """
        return True

    def action(self):
        """
        role : Role
        Search : look around on the Environment
        eat and drink when needed

        Return True if an action was successful
        else False
        """
        if not self.is_alive():
            self.convert_to_food()
            return False

        if self.role == Role.SEARCH:
            supply = self.element.is_supply()
            if supply is not None:
                if self.has_space() == supply.type:
                    self.consume(supply)
                    return True
                else:
                    self.chose_path()
                    return True

            else:
                self.chose_path()
                return True

        return False

    def post(self):
        """
        Print of a Prey
        """
        self.element.post()
        print("Predator")

        if self.is_alive():
            print("id: ", self.id)
            print("size: ", self.size)
            print("State: ", self.role)
            print("Life: ", self.life[0], "out of", self.life[1])
            print("Hunger: ", self.hunger[0], "out of", self.hunger[1])
            print("Thirst: ", self.thirst[0], "out of", self.thirst[1])

            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else:
            print("is dead")