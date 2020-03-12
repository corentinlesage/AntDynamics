from abc import ABC, abstractmethod


class Animal(ABC):
    element = None
    life = list()
    size = None
    damage = None
    hunger = list()
    thirst = list()

    def __init__(self, element,  life, size, damage, hunger, thirst):
        self.element = element
        self.life.append(life)
        self.life.append(life)
        self.size = size
        self.damage = damage
        self.hunger.append(0)
        self.hunger.append(hunger)
        self.thirst.append(0)
        self.thirst.append(thirst)

    def death(self):
        pass

    def receive_damage(self, damage):
        self.life[0] -= damage

        if self.life[0] < 0:
            self.death()
