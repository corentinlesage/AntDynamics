import random

from Programme.Supply import Supply


class Event:
    environment = None
    event = None
    period = None
    delay = None

    def __init__(self, environment, period, delay):

        self.environment = environment
        self.event = -1
        self.period = period
        self.delay = delay

    def launch(self):

        if self.period > 0 and self.event == -1:
            self.period -= 1

        elif self.event == -1:

            event = 0

        if event == 0:
            print("Il pleut !")
            self.rain()

    def rain(self):

        if self.delay == 0:
            self.event = -1
            self.period = random.randint(30, 100)
            self.delay = random.randint(30, 100)
            return False

        element = self.environment.list_element(random.randint(0, len(self.environment.list_element) - 1))

        element.add_supply(Supply(50, -1))

        anthill = self.environment.element_is_entrance(element)

        for i in element.list_animal:
            if not (i.is_ant() and i.home == anthill):
                i.receive_damage(40)

        return True
