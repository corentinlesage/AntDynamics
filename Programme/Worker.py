from Ant import Ant
from Role import Role
from Supply import Supply


class Worker(Ant):

    supply = list()

    def __init__(self, anthill, element, max_storage):
        super(Ant, self).__init__(element, None, None, None, None, None, anthill, None)
        self.role = Role.SEARCH

        self.supply = list()
        self.supply.append(0)
        self.supply.append(max_storage)

    def move_to_element(self, element):

        pheromone = element.get_pheromone()

        if self.role == Role.SEARCH:
            if pheromone.is_detected(0):
                self.role = Role.FLEE
                return False

        if self.role == Role.FLEE or self.role == Role.HARVEST:

            temp = self.find_home_entrance()
            return self.element.distance(temp) >= element.distance(temp) and (not pheromone.is_detected(0))

    def action(self):

        if self.need_rest() != 0:
            self.role == Role.FLEE

        if self.role == Role.SEARCH:
            food = self.element.is_food()
            if food is not None:
                if self.has_space():
                    self. eat(self, food)
                else:
                    self.load(food)
                    self.role = Role.Harvest

            enemy = self.element.is_enemy(self.home)
            if enemy is not None:
                self.role == Role.ATTACK

            else:
                self.chose_path()

        if self.role == Role.HARVEST:
            self.emit_pheromone(1, 0.15)

            if not self.distribute_food():

                if self.element in self.home.entrance:
                    self.store_food()
                    self.role = Role.SEARCH
                else :
                    self.chose_path()

        if self.role == Role.FLEE:
            if self.element in self.home.entrance:
                if self.has_space() != 0 :
                    if not self.eat_base():
                        if not self.drink_base():
                            self.role = Role.SEARCH
                            self.action()

            else:
                self.role == Role.SEARCH
                self.chose_path()

    def load_food(self, food):

        quantity = 0

        if food.size*10 > self.supply[1]:
            quantity = self.supply[1]
            food.size -= self.supply[1]/10

        else:
            quantity = self.food.size*10
            self.element.list_animal.remove(food)
            del food

        self.supply[0] = Supply(quantity, 1)

    def distribute_food(self):

        for i in self.element.list_animal:
            if i.is_ant():
                if i.home == self.home:
                    food_bar = i.has_space()

                    if food_bar == self.supply[0].type:

                        food = 0

                        if self.supply[0].quantity > 10:
                            self.supply[0].quantity -= 10
                            food = 10
                        else:
                            food = self.supply[0].quantity
                            del self.supply
                            self.role == Role.SEARCH

                        if food_bar == 1:
                            i.hunger += food
                        else:
                            i.thirst += food

                        return True
        return False

    def store_food(self):

        ind = None

        if self.supply[0].type == 1:
            ind = 0
        else:
            ind = 1

        self.home.storage[ind] += self.supply[0].quantity

        del self.supply[0]

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
            print("Supply: ", self.supply[0], "out of", self.supply[1])
            if self.is_travelling > 0: print("is travelling for ", self.is_travelling, "turns")

        else: print