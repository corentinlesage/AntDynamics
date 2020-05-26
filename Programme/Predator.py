from Programme.Animal import Animal
from Programme.Role import Role


class Predator(Animal):
    """
    Predator is an Animal
    it attacks every other Animal that are not Predator
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
        Search : look around on the Environment to look for non Predator
        eat and drink when needed

        Attack : When detect an non Predator
        will attack till the end of the fight and pass to Search

        Return True if an action was successful
        else False
        """
        if not self.is_alive():
            self.convert_to_food()

        if self.role == Role.SEARCH:
            supply = self.element.is_supply()
            if supply is not None:
                if self.has_space() == supply.type:
                    self.consume(supply)
                    return True
                else:
                    self.chose_path()
                    return True

            prey = self.element.is_not_predator()
            if prey is not None:
                self.role == Role.ATTACK

            else:
                self.chose_path()
                return True

        if self.role == Role.ATTACK:

            prey = self.element.is_not_predator()

            if prey is not None:

                if prey.is_alive():
                    self.attack(prey)
                    return True

                else:
                    self.role = Role.SEARCH
                    self.action()
                    return True
            else:
                self.role = Role.SEARCH
                self.action()
                return True
        return False

    def is_predator(self):
        return True

    def post(self):
        """
        Print of a Predator
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
            print("Age: ", self.age[0], "out of", self.age[1])

            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else:
            print("is dead")