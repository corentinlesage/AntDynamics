from Programme.Element import Element
from Programme.Path import Path
from Programme.Anthill import Anthill
from Programme.Supply import Supply


class Environment:
    list_element = list()
    list_anthill = list()

    def __init__(self):
        self.list_element = list()
        self.list_anthill = list()

    def add_element(self, radius, capacity, x, y):
        self.list_element.append(Element(radius, capacity, x, y))

    def add_path(self, element1, element2, cost, capacity):
        path = Path(self.list_element[element1], self.list_element[element2], cost, capacity)
        path2 = Path(self.list_element[element2], self.list_element[element1], cost, capacity)

        self.list_element[element1].add_path(path)
        self.list_element[element2].add_path(path2)

    def add_anthill(self, name, list_element):
        list_temp = list()

        for i in list_element:
            list_temp.append(self.list_element[i])

        print("creation of a colony")
        self.list_anthill.append(Anthill(name, list_temp))

    def add_supply(self, element, quantity, type):
        Supply(self.list_element[element], quantity, type)

    def is_entrance(self, element):
        for i in self.list_anthill:
            if element in i.entrance:
                return i

        return None
