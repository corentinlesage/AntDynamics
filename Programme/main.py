from Environment import Environment


def main():
	print('Test 1 Create a basic environment to make an ant travel between 2 elements')
	environment = Environment()

	environment.add_element(1, 1, 0, 0)
	environment.add_element(2, 2, 4, -3)
	environment.add_element(3, 3, -5, 4)

	environment.add_path(0, 1, 1, 1)
	environment.add_path(0, 2, 2, 2)

	environment.add_anthill([0])




main()