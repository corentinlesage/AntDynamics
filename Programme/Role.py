from abc import ABC, abstractmethod


class Role(ABC):

    timeLeft = None

    def __init__(self, time):
        self.timeLeft = time
