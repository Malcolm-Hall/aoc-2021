import sys
sys.path.append("./")
from util import solution_checker

example_input_file = "./02/example-input.txt"
challenge_input_file = "./02/input.txt"

def get_position_and_depth_product(filename, move_fn):
    position = 0
    depth = 0
    aim = 0
    with open(filename) as f:
        for line in f:
            cmd, amt = line.split(" ", 1)
            amt = int(amt)
            position, depth, aim += move_fn(cmd, amt, aim)
                    
    return position * depth

def move_1(cmd, amt, aim):
    match cmd:
        case "forward":
            return amt, 0, 0
        case "down":
            return 0, amt, 0
        case "up":
            return 0, -1*amt, 0
        case _:
            raise Exception("Panic!")

def move_2(cmd, amt, aim):
    match cmd:
        case "forward":
            return amt, aim*amt, 0
        case "down":
            return 0, 0, amt
        case "up":
            return 0, 0, -1*amt
        case _:
            raise Exception("Panic!")

expected_example_product_1 = 15 * 10
expected_example_product_2 = 15 * 60

example_product_1 = get_position_and_depth_product(example_input_file, move_1)
challenge_product_1 = get_position_and_depth_product(challenge_input_file, move_1)

solution_checker(expected_example_product_1, example_product_1, challenge_product_1)

example_product_2 = get_position_and_depth_product(example_input_file, move_2)
challenge_product_2 = get_position_and_depth_product(challenge_input_file, move_2)

solution_checker(expected_example_product_2, example_product_2, challenge_product_2)