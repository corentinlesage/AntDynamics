import Ant


class Soldier(Ant):

    def __init__(self, anthill, element):
        super(Ant, self).__init__(element, None, None, None, None, None, anthill, None)

    def move_to_element(self, element):

        pheromone = element.get_pheromone()

        if pheromone.is_detected(0) and pheromone.is_detected(2):
            # danger enemie dans la zone

