import time

from Environment import Environment


def main():
    print('Test 1 Create a basic environment to make an ant travel between 2 elements')
    environment = Environment()

    environment.add_element(1, 1, 0, 0)
    environment.add_element(2, 2, 4, -3)
    environment.add_element(3, 3, -5, 4)

    environment.add_path(0, 1, 1, 1)
    environment.add_path(0, 2, 2, 2)

    environment.add_anthill("Home", [0])

    n = 1

    while n <= 11:

        print ("\nTurn number", n)

        for i in environment.list_element:

            #i.post()

            for j in i.list_animal:

                j.post()

                if j.alive() and (not j.travelling()):
                    j.action()

        n = n + 1
        #time.sleep(6)


main()
