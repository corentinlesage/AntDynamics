import json
import time

from Programme.Environment import Environment

from Programme.generationJson import serialiseur_perso


def main():
    print('Test 1 Create a basic environment to make an ant travel between 2 elements')
    data = list()
    environment = Environment()

    environment.add_element(1, 5, 0, 0)
    environment.add_element(3, 3, 4, -3)
    environment.add_element(1, 4, -5, 4)

    environment.add_element(3, 7, 3, -4)
    environment.add_element(3, 4, -4, 7)

    environment.add_path(0, 1, 1, 4)
    environment.add_path(0, 2, 2, 4)

    environment.add_path(1, 3, 1, 4)
    environment.add_path(2, 4, 2, 3)

    environment.add_supply(3, 1000, -1)
    environment.add_supply(4, 1000, 1)

    environment.add_anthill("Home", [0])

    n = 1

    while n <= 20:

        print ("\nTurn number", n)

        temp_list_animal = list()

        environment.list_anthill[0].post()

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

        n = n + 1
        data.append(environment)
        #time.sleep(6)

    with open('Test.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=serialiseur_perso)

    for i in environment.list_element:
        i.post()
        print("nombre d'animaux: ", len(i.list_animal))
        print("nombre de tas: ", len(i.list_supply))

        temp = 0
        for j in i.list_path:
            temp += j.capacity[0]

        print("taille total d'animaux en trajets: ", temp)

main()
