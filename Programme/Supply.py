from abc import ABC, abstractmethod

class Supply(ABC):
    quantity = None
    type = None  # food = 1, water = -1

    def __init__(self, quantity, type):
        self.quantity = quantity
        self.type = type
