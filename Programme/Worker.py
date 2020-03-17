import Ant
import Role


class Worker(Ant):

    role = None

    def __init__(self, anthill, element):
        super(Ant, self).__init__(element, None, None, None, None, None, anthill, None)
