from util import Bot

example_input_file = "./input/07-example.txt" 
challenge_input_file = "./input/07.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    with open(filename) as f:
        loc = {}
        exec("input = [" + f.readline() + "]", {}, loc)
        input = loc["input"]
    return input

def calculate_fuel(input, x, fuel_fn):
    fuel_used = [fuel_fn(abs(x - y)) for y in input]
    return sum(fuel_used)

def get_min_fuel(filename, fuel_fn):
    input = parse_input(filename)
    fuel_used_list = []
    for x in range(min(input), max(input)):
        fuel_used_list.append(calculate_fuel(input, x, fuel_fn))
    return min(fuel_used_list)

def fuel_fn_1(distance):
    return distance

def fuel_fn_2(distance):
    return int(distance * (distance + 1) / 2)

expected_min_fuel_1 = 37
expected_min_fuel_2 = 168

bot.check(expected_min_fuel_1, get_min_fuel, [fuel_fn_1])
bot.check(expected_min_fuel_2, get_min_fuel, [fuel_fn_2])