import random

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

    def __init__(self, environment, period, delay):
        """
        Constructor
        """
        self.environment = environment
        self.event = -1
        self.period = period
        self.delay = delay

    def launch(self):
        """
        Launch events when the period is over
        choose a new event at the end of the previous event
        """
        if self.period > 0 and self.event == -1:
            self.period -= 1

        elif self.event == -1:

            self.event = 0

        if self.event == 0:
            print("Il pleut !")
            self.rain()

    def rain(self):
        """
        Generate water that hurt Animal on a random Element picked
        Exception are made for the Ant in there Anthill

        Return True if the event occured
        False if it ended
        """

        if self.delay == 0:
            self.event = -1
            self.period = random.randint(30, 100)
            self.delay = random.randint(30, 100)
            return False

        rand_element = random.randint(0, len(self.environment.list_element) - 1)

        element = self.environment.list_element[rand_element]

        element.add_supply(Supply(element, 50, -1))

        anthill = self.environment.is_entrance(element)

        for i in element.list_animal:
            if not (i.is_ant() and i.home == anthill):
                i.receive_damage(40)

        return True
