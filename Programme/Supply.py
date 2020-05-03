from abc import ABC, abstractmethod


class Supply(ABC):
    element = None
    quantity = None
    type = None  # food = 1, water = -1

    def __init__(self, element, quantity, type):

        self.element = element
        self.quantity = quantity
        self.type = type

    def __delete__(self):
        if self.element is not None:
            self.element.list_supply.remove(self)


    def decomposition(self):
        if self.type == 1:
            self.quantity -= 0.01

            if self.quantity <= 0:
                del self

    def post(self):

        self.element.post()

        temp = ""

        if self.type == -1:
            temp = "Water"
        else: temp = "Food"

        print(temp, ":  ", self.quantity)