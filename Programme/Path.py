class Path:
	
	start = None
	end = None
	
	cost = None
	max_capacity = None
	capacity = None

	def __init__(self, start, end, cost, max_capacity):
		self.start = start
		self.end = end
		self.cost = cost
		self.max_capacity = max_capacity
		capacity = 0