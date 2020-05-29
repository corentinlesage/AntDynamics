import json
import copy

from Programme.Environment import Environment
from Programme.Event import Event
from Programme.generationJson import serialiseur_perso

def main():
    print('Test 1 Create a basic environment')
    environment = Environment()
    data = list()

    environment.add_element(4, 15, 10, 10)
    environment.add_element(3, 12, 12, 10)
    environment.add_element(2, 21, 11, 8)
    environment.add_element(4, 16, 6, 10)
    environment.add_element(3, 10, 10, 12)
    environment.add_element(1, 20, 14, 12)
    environment.add_element(3, 14, 16, 8)
    environment.add_element(4, 18, 14, 6)

    environment.add_path(0, 1, 1, 21)
    environment.add_path(0, 2, 1, 17)
    environment.add_path(0, 4, 2, 16)

    environment.add_path(1, 2, 1, 19)
    environment.add_path(1, 5, 2, 12)
    environment.add_path(1, 6, 3, 17)

    environment.add_path(2, 3, 3, 14)
    environment.add_path(2, 7, 2, 15)

    environment.add_path(3, 4, 3, 14)

    environment.add_path(4, 5, 3, 12)

    environment.add_path(6, 7, 3, 15)

    environment.add_supply(3, 300, -1)

    environment.add_supply(5, 300, 1)

    environment.add_supply(6, 300, -1)
    environment.add_supply(6, 300, 1)

    environment.add_anthill("Home", [0])

    environment.event = Event(environment)

    n = 1

    while n <= 200:#1000

        print("\nTurn number", n)

        environment.event.launch()

        temp_list_animal = list()

        environment.list_anthill[0].post()

        data.append(copy.deepcopy(environment))

        for i in environment.list_element:

            i.pheromone.decrease()

            for j in i.list_supply:
                j.post()
                j.decomposition()

            for j in i.list_animal:

                if j not in temp_list_animal:
                    temp_list_animal.append(j)
                    j.post()

                    if j.alive():
                        if not j.travelling():
                            j.action()
                    else:
                        j.convert_to_food()

        n = n + 1
        # time.sleep(6)

    for i in environment.list_element:

        if len(i.list_supply) == 0 and len(i.list_animal) == 0:
            pass

        else:
            i.post()

    with open('Data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=serialiseur_perso)

main()
