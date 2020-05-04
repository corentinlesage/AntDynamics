from Programme.Ant import Ant
from Programme.Role import Role


class Queen(Ant):

    def __init__(self, anthill, element):
        super(Ant, self).__init__(element, None, None, None, None, None, anthill, None)
        self.role = Role.PASSIVE

