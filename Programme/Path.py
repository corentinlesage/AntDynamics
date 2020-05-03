class Path:
    start = None
    end = None

    cost = None
    capacity = list()

    def __init__(self, start, end, cost, max_capacity):
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
