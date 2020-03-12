import Element
import Ant
from Queen import Queen


class Anthill:
    entrance = list()
    colony = list()

    def __init__(self, entrance):
        self.entrance = entrance
        self.colony.append(Queen(self))
