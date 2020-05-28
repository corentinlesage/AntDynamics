from Programme.Element import Element
from Programme.Path import Path
from Programme.Anthill import Anthill
from Programme.Supply import Supply


class Environment:
    """
    Environment is a graph composed of Element as summits and Paths as ridges
    it is the background were Animal, Event, and Anthill interact

    list_element : list of Element
    list_anthill : list of Anthill
    """
    list_element = list()
    list_anthill = list()
    event = None

    def __init__(self):
        """
        Constructor
        """
        self.list_element = list()
        self.list_anthill = list()
        self.event = None

    def add_element(self, radius, capacity, x, y):
        """
        Create an element in the environment from the paramaters given
        radius : positive integer, capacity : positive integer, x : real number, y : real number
        """
        self.list_element.append(Element(radius, capacity, x, y))

    def add_path(self, element1, element2, cost, capacity):
        """
        Create a bidirectional path in the environment from the parameters given
        element1 : Element, element2 : Element, cost : positive integer, capacity : positive integer
        """
        path = Path(self.list_element[element1], self.list_element[element2], cost, capacity)
        path2 = Path(self.list_element[element2], self.list_element[element1], cost, capacity)

        self.list_element[element1].add_path(path)
        self.list_element[element2].add_path(path2)

    def add_anthill(self, name, list_element):
        """
        Create an anthill in the environment from the parameters given
        name : String, list_element : list of Element
        """

        list_temp = list()

        for i in list_element:
            list_temp.append(self.list_element[i])

        print("creation of a colony")
        self.list_anthill.append(Anthill(name, list_temp))

    def add_supply(self, element, quantity, type):
        """
        Create a supply in the environment from the parameters given
        element : Element, quantity real : positive number, type : 1 or -1
        """
        Supply(self.list_element[element], quantity, type)

    def is_entrance(self, element):
        """
        Verify if an element from the environment correspond to an entrance of an anthill
        return the anthill if its a match
        else None
        """
        for i in self.list_anthill:
            if element in i.entrance:
                return i

        return None
