import math

class Position:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, position):
        return math.sqrt(math.pow(self.x - position.x) + math.pow(self.y - position.y))

    def post(self):
        print("position:", self.x, self.y)