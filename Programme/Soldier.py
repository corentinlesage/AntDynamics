from Programme.Ant import Ant
from Programme.Role import Role


class Soldier(Ant):
    """
    Soldier is an Ant
    It wonder of the Environment to look for intruders : Prey, Predator and other Anthill
    to defend his Anthill from
    """
    def __init__(self, anthill, element):
        """
        Constructor
        """
        Ant.__init__(self, element, 80, 2, 3, 80, 80, anthill, 500)
        self.role = Role.SEARCH



    def move_to_element(self, element):
        """
        Soldier try to wonder of the Environment to look for intruders in Role : Search

        element : Element
        Return True if the Element is valid
        else False
        """
        pheromone = element.get_pheromone()

        if self.role == Role.SEARCH:
            temp = pheromone.is_detected(0)
            if temp and pheromone.is_detected(2):

                self.role = Role.ATTACK
                self.emit_pheromone(0, 0.15)
                self.emit_pheromone(2, 0.15)

                return True

            elif temp:
                self.role = Role.FLEE
                return False

            else:
                return True

        if self.role == Role.FLEE or self.role == Role.REST:
            temp = self.find_home_entrance()
            return self.element.distance(temp) >= element.distance(temp) and (not pheromone.is_detected(0))

    def action(self):
        """"
        role : Role
        Search : look around on the Environment to look for intruders
        If Supply detected, emit food Pheromone
        If hurt emit a danger Pheromone
        If danger pheromone is detected pass to Flee
        If hungry or thirsty, pass to Rest

        Flee : Reach safety to the colony as quickly as possible
        pass to Search if no more danger Pheromone is detected

        Rest : Reach the colony to eat and drink then pass to Search

        Attack : When detect an intruder or sense a signal of Pheromone of an intruder
        will attack till the end of the fight and pass to Search

        Return True if an action was successful
        else False
        """

        if not self.is_alive():
            self.convert_to_food()
            return False

        if self.need_rest() != 0 and self.role != Role.ATTACK:
            self.role = Role.REST

        if self.role == Role.SEARCH:
            supply = self.element.is_supply()
            if supply is not None:
                self.emit_pheromone(1, 0.15)

                if self.has_space() == supply.type:
                    self.consume(supply)
                    return True
                else:
                    self.chose_path()
                    return True

            enemy = self.element.is_enemy(self.home)
            if enemy is not None:
                self.role == Role.ATTACK

            else:
                self.chose_path()
                return True

        if self.role == Role.ATTACK:

            enemy = self.element.is_enemy(self.home)

            if enemy is not None:

                if enemy.is_alive():
                    self.emit_pheromone(0, 0.15)
                    self.emit_pheromone(2, 0.15)
                    self.attack(enemy)
                    return True

                else:
                    self.role = Role.SEARCH
                    self.action()
                    return True
            else:
                self.role = Role.SEARCH
                self.action()
                return True

        if self.role == Role.FLEE or self.role == Role.REST:
            if self.element in self.home.entrance:
                self.role = Role.REST

                if self.has_space() != 0:
                    if not self.consume_base():
                        self.role = Role.SEARCH
                        self.action()
                        return True

                    if self.has_space() != 0:
                        return True

            else:
                if self.role == Role.FLEE:
                    self.emit_pheromone(0, 0.15)
                self.chose_path()
                return True
        return False

    def post(self):
        """
        Print af a Soldier
        """
        self.element.post()
        print("soldier ant from the colony ", self.home.name)

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
