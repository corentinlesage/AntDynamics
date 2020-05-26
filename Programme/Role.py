from enum import Enum


class Role(Enum):
    """
    State that can take Animal
    """
    PASSIVE = 1
    SEARCH = 2
    FLEE = 3
    REST = 4
    ATTACK = 5
    HARVEST = 6
