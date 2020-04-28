import random


class Pheromone:
    pheromone = list()

    def __init__(self, danger, food, recruit):

        self.pheromone = list()
        self.pheromone.append(danger)
        self.pheromone.append(food)
        self.pheromone.append(recruit)

    def decrease(self):
        for i in self.pheromone:
            if i > 0.5:
                i -= 0.05
            else:
                i = 0

    def add_pheromone(self, p, quantity):
        self.pheromone[p] += quantity

    def is_detected(self, p):
        return self.pheromone[p] > random.random()

    def post(self):
        print("danger: ", self.pheromone[0])
        print("food: ", self.pheromone[1])
        print("recruit: ", self.pheromone[2])
