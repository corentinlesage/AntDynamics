import random

from Programme.Predator import Predator
from Programme.Prey import Prey
from Programme.Supply import Supply


class Event:
    """
    Event generate random events on the Environment

    event is the event actually occurring on the map
    period is time in turn number until the event is launch
    delay is the time during the event is still in process

    environment : Environment
    event : number of the event occurring between 0 and 10
    default value at -1
    period : time in
    delay = None
    """
    environment = None
    event = None
    period = None
    delay = None

    def __init__(self, environment):
        """
        Constructor
        """
        self.environment = environment
        self.event = -1
        self.period = -1
        self.delay = 0

    def launch(self):
        """
        Launch events when the period is over
        choose a new event at the end of the previous event

        Return True if a new Event has been launch
        Else return False
        """
        if self.delay == 0:
            self.event = random.random()
            self.period = random.randint(30, 100)
            self.delay = -1
            return True

        if self.period > 0:
            self.period -= 1

        else:

            if self.event <= 0.2:
                print("Il pleut")
                self.rain()

            elif 0.2 < self.event <= 0.7:
                print("Nourriture")
                self.food()

            elif 0.7 < self.event <= 0.71:
                print("Predateur")
                self.predator()

            else:
                print("Proie")
                self.prey()

        return False

    def rain(self):
        """
        Generate water that hurt Animal on a random Element picked
        Exception are made for the Ant in their Anthill
        """
        if self.delay == -1:
            self.delay = 9
        else:
            self.delay -= 1

        rand_element = random.randint(0, len(self.environment.list_element) - 1)
        element = self.environment.list_element[rand_element]

        Supply(element, 50, -1)

        anthill = self.environment.is_entrance(element)

        for i in element.list_animal:
            if not (i.is_ant() and i.home == anthill):
                i.receive_damage(20)

    def food(self):
        """
        Generate food that except were Anthills are
        """
        if self.delay == -1:
            self.delay = 0
        else:
            self.delay -= 1

        rand_element = random.randint(0, len(self.environment.list_element) - 1)
        element = self.environment.list_element[rand_element]

        anthill = True

        while anthill:

            rand_element = random.randint(0, len(self.environment.list_element) - 1)
            element = self.environment.list_element[rand_element]

            if self.environment.is_entrance(element) is not None:
                anthill = True
            else:
                anthill = False

        Supply(element, 50, 1)

    def predator(self):
        """
        Generate a Predator on a random element except were Anthills are
        """
        if self.delay == -1:
            self.delay = 0
        else:
            self.delay -= 1
        anthill = True

        while anthill:

            rand_element = random.randint(0, len(self.environment.list_element) - 1)
            element = self.environment.list_element[rand_element]

            if self.environment.is_entrance(element) is not None:
                anthill = True
            else:
                anthill = False

        element.add_animal(Predator(element, 200, 5, 10, 50, 50))

    def prey(self):
        """
        Generate a Prey on a random element except were Anthills are
        """
        if self.delay == -1:
            self.delay = 0
        else:
            self.delay -= 1

        anthill = True

        while anthill:

            rand_element = random.randint(0, len(self.environment.list_element) - 1)
            element = self.environment.list_element[rand_element]

            if self.environment.is_entrance(element) is not None:
                anthill = True
            else:
                anthill = False

        element.add_animal(Prey(element, 200, 8, 1, 100, 100))
