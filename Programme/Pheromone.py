from random import random


class Pheromone:
    pheromone = list()

    def __init__(self, danger, food, recruit):
        self.pheromone.append(danger)
        self.pheromone.append(food)
        self.pheromone.append(recruit)

    def decrease(self):
        for i in self.pheromone:
            i -= 5
            if i < 0:
                i = 0

    def is_detected(self, p):
        return self.pheromone[p] <= random.random()
