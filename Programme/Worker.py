from Programme.Ant import Ant
from Programme.Role import Role
from Programme.Supply import Supply


class Worker(Ant):
    supply = list()

    def __init__(self, anthill, element, max_storage):
        Ant.__init__(self, element, 100, 1, 0, 100, 100, anthill, 500)
        self.role = Role.SEARCH

        self.supply = list()
        self.supply.append(None)
        self.supply.append(max_storage)

    def move_to_element(self, element):

        pheromone = element.get_pheromone()

        if self.role == Role.SEARCH:
            if pheromone.is_detected(0):
                self.role = Role.FLEE
                return False
        return True

        if self.role == Role.FLEE or self.role == Role.HARVEST or self.role == Role.REST:
            temp = self.find_home_entrance()
            return self.element.distance(temp) >= element.distance(temp) and (not pheromone.is_detected(0))

    def action(self):

        if not self.is_alive():
            self.convert_to_food()

        if self.need_rest() != 0 and self.role != Role.HARVEST:
            self.role = Role.REST

        if self.role == Role.SEARCH:
            supply = self.element.is_supply()
            if supply is not None:
                if self.has_space() == supply.type:
                    self.consume(supply)
                    return True
                else:
                    self.load(supply)
                    self.role = Role.HARVEST
                    return True

            enemy = self.element.is_enemy(self.home)
            if enemy is not None:
                self.role = Role.FLEE

            else:
                self.chose_path()
                return True

        if self.role == Role.HARVEST:
            self.emit_pheromone(1, 0.15)

            if self.distribute():
                return True
            else:

                if self.element in self.home.entrance:
                    self.store()
                    self.role = Role.SEARCH
                    return True

                else:
                    self.chose_path()
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

    def load(self, supply):

        quantity = 0

        if supply.quantity > self.supply[1]:
            quantity = self.supply[1]
            supply.quantity -= self.supply[1]

        else:
            quantity = supply.quantity
            del supply

        self.supply[0] = Supply(None, quantity, supply.type)

    def distribute(self):

        for i in self.element.list_animal:
            if i.is_ant():
                if i.home == self.home and i != self:
                    bar = i.has_space()

                    if bar == self.supply[0].type:

                        food = 0

                        if self.supply[0].quantity > 10:
                            self.supply[0].quantity -= 10
                            food = 10
                        else:
                            food = self.supply[0].quantity
                            self.supply[0].__delete__()
                            self.supply[0] = None

                            self.role = Role.SEARCH

                        if bar == 1:
                            i.hunger[0] += food
                        else:
                            i.thirst[0] += food

                        return True
        return False

    def store(self):

        ind = None

        if self.supply[0].type == 1:
            ind = 0
        else:
            ind = 1

        self.home.storage[ind] += self.supply[0].quantity

        self.supply[0].__delete__()
        self.supply[0] = None

    def post(self):

        self.element.post()
        print("worker ant from the colony ", self.home.name)

        if self.is_alive():
            print("size: ", self.size)
            print("State: ", self.role)
            print("Life: ", self.life[0], "out of", self.life[1])
            print("Hunger: ", self.hunger[0], "out of", self.hunger[1])
            print("Thirst: ", self.thirst[0], "out of", self.thirst[1])
            print("Age: ", self.age[0], "out of", self.age[1])

            temp = 0

            if self.supply[0] is not None:
                temp = self.supply[0].quantity

            print("Supply: ", temp, "out of", self.supply[1])

            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else:
            print("is dead")
