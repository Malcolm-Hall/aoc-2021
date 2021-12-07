from util import solution_checker, Bot

example_input_file = "./input/06-example.txt"
challenge_input_file = "./input/06.txt"
bot = Bot(example_input_file, challenge_input_file)

def get_population_map():
    return {i:0 for i in range(9)}

def simulate_laternfish(filename, num_days):
    with open(filename) as f:
        loc = {}
        exec("initial_lanternfish = [" + f.readline() + "]", {}, loc)
        initial_laternfish = loc["initial_lanternfish"]

    lanternfish_population = get_population_map()
    for lanternfish in initial_laternfish:
        lanternfish_population[lanternfish] += 1


    for _ in range(num_days):
        new_population = get_population_map()
        for key, value in lanternfish_population.items():
            if key == 0:
                new_population[6] += value
                new_population[8] += value
            else:
                new_population[key - 1] += value
        lanternfish_population = new_population
        
    num_lanternfish = 0
    for value in lanternfish_population.values():
        num_lanternfish += value
    return num_lanternfish

expected_number_of_lanternfish_1 = 5934
expected_number_of_lanternfish_2 = 26984457539

bot.check(expected_number_of_lanternfish_1, simulate_laternfish, [80])
bot.check(expected_number_of_lanternfish_2, simulate_laternfish, [256])
