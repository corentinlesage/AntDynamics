from Programme.Animal import Animal
from Programme.Ant import Ant
from Programme.Anthill import Anthill
from Programme.Egg import Egg
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
import json

class test():
    def __init__(self):
        return

"""
    function which transform the objects in json object 
    to send data to front-end
"""

def serialiseur_perso(obj):
    # parent class are always under child class in this function

    if isinstance(obj, Queen):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant
        return {"__class__": "Queen",
                "lay_rate": obj.lay_rate,
                "__parent__": serialiseur_perso(obj_cpy)
                }


    if isinstance(obj, Soldier):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant
        return {"__class__": "Soldier",
                "__parent__": serialiseur_perso(obj_cpy)
                }

    if isinstance(obj, Egg):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant
        return {"__class__": "Egg",
                "hatch": obj.hatch,
                "__parent__": serialiseur_perso(obj_cpy)
                }

    if isinstance(obj, Worker):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Ant
        if (obj.supply[0] == None) :
            return {"__class__": "Worker",
                    "supply_capacity": obj.supply[1],
                    "supply": "nothing",
                    "__parent__": serialiseur_perso(obj_cpy)
                    }
        else:
            return {"__class__": "Worker",
                    "supply_capacity": obj.supply[1],
                    "supply": serialiseur_perso(obj.supply[0]),
                    "__parent__": serialiseur_perso(obj_cpy)
                    }


    if isinstance(obj, Ant):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Animal
        return {"__class__": "Ant",
                "home": obj.home.name,
                "age": obj.age[0],
                "age_max": obj.age[1],
                "role": str(obj.role),
                "__parent__": serialiseur_perso(obj_cpy)
                }

    if isinstance(obj, Animal):
        if obj.is_travelling > 0:
            return {"__class__": "Animal",
                    "id": obj.id,
                    #"element": obj.element,
                    "life": obj.life[0],
                    "life_max": obj.life[1],
                    "size": obj.size,
                    "damage": obj.damage,
                    "hunger": obj.hunger[0],
                    "hunger_max": obj.hunger[1],
                    "thirst": obj.thirst[0],
                    "thirst_max": obj.thirst[1],
                    "is_travelling": obj.is_travelling,
                    "origin": obj.path.get_start().id
                    }
        else:
            return {"__class__": "Animal",
                    "id": obj.id,
                    #"element": obj.element,
                    "life": obj.life[0],
                    "life_max": obj.life[1],
                    "size": obj.size,
                    "damage": obj.damage,
                    "hunger": obj.hunger[0],
                    "hunger_max": obj.hunger[1],
                    "thirst": obj.thirst[0],
                    "thirst_max": obj.thirst[1],
                    "is_travelling": obj.is_travelling,
                    }

    if isinstance(obj, Anthill):
        return {"__class__": "Anthill",
                "name": obj.name,
                "entrance": generationListe(obj.entrance),
                "colony": generationListe(obj.colony),
                "storage": obj.storage
                }

    if isinstance(obj, Element):
        return {"__class__": "Element",
                "id": obj.id,
                "radius": obj.radius,
                "capacity": obj.capacity[0],
                "capacity_max": obj.capacity[1],
                "position": serialiseur_perso(obj.position),
                "pheromone": serialiseur_perso(obj.pheromone),
                "list_animal": generationListe(obj.list_animal),
                "list_path": generationListe(obj.list_path),
                "list_supply": generationListe(obj.list_supply)
                }

    if isinstance(obj, Environment):
        return {"__class__": "Environment",
                "list_element": generationListe(obj.list_element),
                "list_anthill": generationListe(obj.list_anthill)
                }

    if isinstance(obj, Path):
        return {"__class__": "Path",
                "id": obj.id,
                "start": obj.start.id,
                "end": obj.end.id,
                "cost": obj.cost,
                "capacity": obj.capacity[0],
                "capacity_max": obj.capacity[1],
                }

    if isinstance(obj, Pheromone):
        return {"__class__": "Pheromone",
                "pheromone_danger": obj.pheromone[0],
                "pheromone_food": obj.pheromone[1],
                "pheromone_recruit": obj.pheromone[2]
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

"""
    function which transform a list of object to a json list of object
"""
def generationListe(liste):
    generate = list()
    for elem in liste:
        generate.append(serialiseur_perso(elem))
    return generate

"""
    function which transform a list of int to a string 
"""
def generationListeEntier(liste):
    generate = ""
    for elem in liste:
        generate += str(elem) + " , "
    return generate.strip(" , ")
