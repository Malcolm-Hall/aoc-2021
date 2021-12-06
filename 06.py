import sys
sys.path.append("./")
from util import solution_checker 

example_input_file = "./06/example-input.txt"
challenge_input_file = "./06/input.txt"

class LanternfishEvolver:
    children = 0
    def evolve(self, lanternfish):
        if lanternfish == 0:
            self.children += 1
            lanternfish = 6
        else:
            lanternfish -= 1
        return lanternfish
    
    def breed(self):
        children = self.children
        self.children = 0
        return [8 for _ in range(children)]

def simulate_laternfish(filename, num_days):
    with open(filename) as f:
        loc = {}
        exec("initial_lanternfish = [" + f.readline() + "]", {}, loc)
        initial_laternfish = loc["initial_lanternfish"]

    lanternfish_population = initial_laternfish
    evolver = LanternfishEvolver()
    for _ in range(num_days):
        lanternfish_population = [evolver.evolve(lanternfish) for lanternfish in lanternfish_population]
        lanternfish_population.extend(evolver.breed())
        
    num_lanternfish = 0
    for _ in lanternfish_population:
        num_lanternfish += 1
    return num_lanternfish

expected_example_number_of_lanternfish_1 = 5934
expected_example_number_of_lanternfish_2 = 26984457539

example_number_of_lanternfish_1 = simulate_laternfish(example_input_file, 80)
challenge_number_of_lanternfish_1 = simulate_laternfish(challenge_input_file, 80)

solution_checker(expected_example_number_of_lanternfish_1, example_number_of_lanternfish_1, challenge_number_of_lanternfish_1)

example_number_of_lanternfish_2 = simulate_laternfish(example_input_file, 256)
# challenge_number_of_lanternfish_2 = simulate_laternfish(challenge_input_file, 256)

solution_checker(expected_example_number_of_lanternfish_2, example_number_of_lanternfish_2, 0)#challenge_number_of_lanternfish_2)