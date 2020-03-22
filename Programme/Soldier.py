from Ant import Ant
from Role import Role


class Soldier(Ant):

    def __init__(self, anthill, element):
        Ant.__init__(self, element, 10, 2, 3, 10, 10, anthill, 100)
        self.role = Role.SEARCH

    def move_to_element(self, element):

        pheromone = element.get_pheromone()

        if self.role == Role.SEARCH:
            temp = pheromone.is_detected(0)
            if temp and pheromone.is_detected(2):
                return True

            elif temp:
                self.Role = Role.FLEE
                return False

        elif self.role == Role.FLEE:
            temp = self.find_home_entrance()
            return self.element.distance(temp) >= element.distance(temp) and (not pheromone.is_detected(0))

    def action(self):
        if self.role == Role.SEARCH:
            if self.element.is_food() is not None:
                self.emit_pheromone(1, 0.15)
                self.chose_path()

            enemy = self.element.is_enemy(self.home)
            if enemy is not None:
                self.role == Role.ATTACK

            else:
                self.chose_path()

        if self.role == Role.ATTACK:
            if not enemy.is_alive():
                self.role = Role.SEARCH
                self.action()
            else:
                self.emit_pheromone(0, 0.15)
                self.emit_pheromone(2, 0.15)
                self.attack(enemy)


    def post(self):

        self.element.post()
        print("soldier ant from the colony ", self.home.name)

        if self.is_alive():
            print("size: ", self.size)
            print("State: ", self.role)
            print("Life: ", self.life[0], "out of", self.life[1])
            print("Hunger: ", self.hunger[0], "out of", self.hunger[1])
            print("Thirst: ", self.thirst[0], "out of", self.thirst[1])
            print("Age: ", self.age[0], "out of", self.age[1])
            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else: print("is dead")