import random


class Pheromone:
    """
    Pheromone is a representation of the pheromones used by Ant to navigate in Environment
    Ant put Pheromone on Element to send a message to other Ant
    The pheromone rates is a real number between 0 and 1

    pheromone = list of the three pheromones possibly present on an Element
    1. danger : warn against a threat on the Element
    2. food : signal some water or food on the Element
    3. recruit : signal some help needed against an intruder
    """
    pheromone = list()

    def __init__(self, danger, food, recruit):
        """
        Constructor
        """
        self.pheromone = list()
        self.pheromone.append(danger)
        self.pheromone.append(food)
        self.pheromone.append(recruit)

    def decrease(self):
        """
        Decrease the pheromones each turn
        """
        for i in self.pheromone:
            if i > 0.05:
                i -= 0.05
            else:
                i = 0

    def add_pheromone(self, p, quantity):
        """
        Add the pheromone requested depending of the type p of pheromone and the quantity
        p : number 0, 1 or 2
        quantity : real number between 0 and 1
        """
        if self.pheromone[p] + quantity <= 1:
            self.pheromone[p] += quantity
        else:
            self.pheromone[p] = 1

    def is_detected(self, p):
        """
        Verify if the pheromone p of Element is detected by the Ant looking for it
        the higher the pheromone rate is, the higher chances are to detect it

        p : number 0, 1 or 2
        """
        return self.pheromone[p] > random.random()

    def post(self):
        """
        Print of the Pheromone
        """
        print("danger: ", self.pheromone[0])
        print("food: ", self.pheromone[1])
        print("recruit: ", self.pheromone[2])
