class Path:
    """
    Path serves to link two Element
    and where Animal travels

    the id helps identify an path individually
    it has a start, an end, a cost and a maximum capacity
    cost corresponds to the time of travel in number of turns

    ID : positive integer
    id : positive integer
    start : Element
    end : Element
    cost : positive integer
    capacity : list of two values
    1. actual capacity of Element
    2. capacity max of Element
    """
    ID = 0
    id = None
    start = None
    end = None

    cost = None
    capacity = list()

    def __init__(self, start, end, cost, max_capacity):
        """
        Constructor
        """
        self.id = Path.ID
        Path.ID += 1

        self.start = start
        self.end = end
        self.cost = cost

        self.capacity = list()
        self.capacity.append(0)
        self.capacity.append(max_capacity)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
