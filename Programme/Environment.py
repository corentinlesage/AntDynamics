from Element import Element
from Path import Path
from Anthill import Anthill


class Environment:
    list_element = list()
    list_anthill = list()

    def __init__(self):
        self.list_element = list()
        self.list_anthill = list()

    def add_element(self, radius, capacity, x, y):
        self.list_element.append(Element(radius, capacity, x, y))

    def add_path(self, element1, element2, cost, capacity):
        if len(self.list_element) > element1 or len(self.list_element) > element2:
            return False

        path = Path(self.list_element[element1], self.list_element[element2], cost, capacity)

        self.list_element[element1].append(path)
        self.list_element[element2].append(path)

        return True

    def add_anthill(self, list_element):
        for i in list_element:
            if len(self.list_element) > i:
                return False

        list_temp = list()

        for i in list_element:
            list_temp.append(self.list_element[i])

        self.list_anthill.append(Anthill(list_temp))

        return True
