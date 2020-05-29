from Programme.Ant import Ant
from Programme.Role import Role
from Programme.Supply import Supply


class Worker(Ant):
    """
    Worker is an Ant
    It wonder of the Environment to look for Supply to store in his Anthill

    supply : List
    1. Supply or None if empty
    2. max_storage : positive integer
    """
    supply = list()

    def __init__(self, anthill, element, max_storage):
        """
        Constructor
        """
        Ant.__init__(self, element, 100, 1, 0, 100, 100, anthill, 500)
        self.role = Role.SEARCH

        self.supply = list()
        self.supply.append(None)
        self.supply.append(max_storage)

    def __delete__(self):
        """
        Destructor

        The Supply carried by the Worker is put on the Element of the Worker death
        """
        if self.supply[0] is not None:
            self.element.add_supply(self.supply[0])
            self.supply[0].element = self.element
        super().__delete__()

    def move_to_element(self, element):
        """
        Worker try to wonder of the Environment to look for Supply in the Role : Search

        element : Element
        Return True if the Element is valid
        else False
        """
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
        """"
        role : Role
        Search : look around on the Environment to look for Supply
        If Supply detected, emit food pass to Harvest
        If hurt emit a danger Pheromone
        If danger pheromone is detected pass to Flee
        If hungry or thirsty, pass to Rest

        Flee : Reach safety to the colony as quickly as possible
        pass to Search if no more danger Pheromone is detected

        Rest : Reach the colony to eat and drink then pass to Search

        Harvest : When a Supply is detected or the food Pheromone is detected
        harvest the supply and go to its Anthill to store it
        will also distribute the food to other Ant of the same Anthill on the way
        then pass to Search

        Return True if an action was successful
        else False
        """
        if not self.is_alive():
            self.convert_to_food()
            return False

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
        """
        Worker in Harvest load Supply for transport

        supply : Supply
        """
        quantity = 0
        type = supply.type

        if supply.quantity > self.supply[1]:
            quantity = self.supply[1]
            supply.quantity -= self.supply[1]

        else:
            quantity = supply.quantity
            del supply

        self.supply[0] = Supply(None, quantity, type)

    def distribute(self):
        """
        Worker in Harvest distribute the Supply to other Ant in need if encountered
        """
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
        """
        Worker in Harvest depose the Supply in the store of their Anthill
        """
        ind = None

        if self.supply[0].type == 1:
            ind = 0
        else:
            ind = 1

        self.home.storage[ind] += self.supply[0].quantity

        self.supply[0].__delete__()
        self.supply[0] = None

    def post(self):
        """
        Print of a Worker
        """
        self.element.post()
        print("worker ant from the colony ", self.home.name)

        if self.is_alive():
            print("id: ", self.id)
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
