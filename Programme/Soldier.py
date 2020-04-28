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

                self.role = Role.ATTACK
                self.emit_pheromone(0, 0.15)
                self.emit_pheromone(2, 0.15)

                return True

            elif temp:
                self.role = Role.FLEE
                return False

            else:
                return True

        if self.role == Role.FLEE:

            temp = self.find_home_entrance()
            return self.element.distance(temp) >= element.distance(temp) and (not pheromone.is_detected(0))

    def action(self):

        if self.need_rest() != 0:
            self.role == Role.FLEE

        if self.role == Role.SEARCH:
            food = self.element.is_food()
            if food is not None:
                self.emit_pheromone(1, 0.15)

                if self.has_space():
                    self.eat(self, food)
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
            else :
                self.role = Role.SEARCH
                self.action()
                return True

        if self.role == Role.FLEE:
            if self.element in self.home.entrance:
                if self.has_space() != 0:
                    if not self.eat_base():
                        if not self.drink_base():
                            self.role = Role.SEARCH
                            self.action()
                            return True

            else:
                self.role == Role.SEARCH
                self.chose_path()
                return True
        return False


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