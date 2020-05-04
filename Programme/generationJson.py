from Programme.Animal import Animal
from Programme.Ant import Ant
from Programme.Anthill import Anthill
from Programme.Element import Element
from Programme.Environment import Environment
from Programme.Path import Path
from Programme.Pheromone import Pheromone
from Programme.Position import Position
from Programme.Queen import Queen
from Programme.Worker import Worker
from Programme.Soldier import Soldier
from Programme.Supply import Supply


import copy

class test():
    def __init__(self):
        return




def serialiseur_perso(obj):
    # parent class are always under child class in this function

    if isinstance(obj, Queen):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant

    if isinstance(obj, Soldier):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant

    if isinstance(obj, Worker):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant

    if isinstance(obj, Ant):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Animal
        return {"__class__": "Ant",
                #"home": obj.home,
                "age": generationListeEntier(obj.age),
                "role": str(obj.role),
                "__parent__": serialiseur_perso(obj_cpy)
                }

    if isinstance(obj, Animal):
        return {"__class__": "Animal",
                #"element": obj.element,
                "life": generationListeEntier(obj.life),
                "size": str(obj.size),
                "damage": str(obj.damage),
                "hunger": generationListeEntier(obj.hunger),
                "thirst": generationListeEntier(obj.thirst),
                "is_travelling": str(obj.is_travelling)}

    if isinstance(obj, Anthill):
        return {"__class__": "Anthill",
                "name": obj.name,
                "entrance": generationListe(obj.entrance),
                "colony": generationListe(obj.colony),
                "storage": obj.storage
                }

    if isinstance(obj, Element):
        return {"__class__": "Element",
                "radius": obj.radius,
                "capacity": generationListeEntier(obj.capacity),
                "position": serialiseur_perso(obj.position),
                "pheromone": serialiseur_perso(obj.pheromone),
                "list_animal": generationListe(obj.list_animal),
                "list_path": generationListe(obj.list_path)
                }

    if isinstance(obj, Environment):
        return {"__class__": "Environment",
                "list_element": generationListe(obj.list_element),
                "list_anthill": generationListe(obj.list_anthill)
                }

    if isinstance(obj, Path):
        return {"__class__": "Path",
                # "start": serialiseur_perso(obj.start),
                # "end": serialiseur_perso(obj.end),
                "cost": obj.cost,
                "capacity": generationListeEntier(obj.capacity)
                }

    if isinstance(obj, Pheromone):
        return {"__class__": "Pheromone",
                "pheromone": generationListeEntier(obj.pheromone)
                }

    if isinstance(obj, Position):
        return {"__class__": "Position",
                "x": obj.x,
                "y": obj.y
                }

    if isinstance(obj, Supply):
        return {"__class__": "Supply",
                "quantity": obj.quantity,
                "type": obj.type}

    raise TypeError(repr(obj) + " n'est pas sérialisable !")


def generationListe(liste):
    generate = "["
    for elem in liste:
        generate += "{ "+ str(serialiseur_perso(elem)) +" }"
    return generate + "]"


def generationListeEntier(liste):
    generate = ""
    for elem in liste:
        generate +=  str(elem) + " , "
    return generate
