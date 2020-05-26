import math


class Position:
    """
    Position are coordinates in a two dimensions graphic

    x : real number
    y: real number
    """
    x = None
    y = None

    def __init__(self, x, y):
        """
        Constructor
        """
        self.x = x
        self.y = y

    def distance(self, position):
        """
        Return the calculus of the distance between two coordinates
        """
        return math.sqrt(math.pow(self.x - position.x, 2) + math.pow(self.y - position.y, 2))

    def post(self):
        """"
        Print of the Position
        """
        print("position:", self.x, self.y)
