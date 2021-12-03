import sys
sys.path.append("C:\\dev\\aoc-2021")
from util import solution_checker

def get_position_and_depth_product_1(filename):
    position = 0
    depth = 0

    with open(filename) as f:
        for line in f:
            cmd, amt = line.split(" ", 1)
            amt = int(amt)
            match cmd:
                case "forward":
                    position += amt
                case "backward":
                    position -= amt
                case "down":
                    depth += amt
                case "up":
                    depth -= amt
                case _:
                    print("Panic!")
                    
    # print(f"{filename=} {position=} {depth=}")
    return position * depth

def get_position_and_depth_product_2(filename):
    position = 0
    depth = 0
    aim = 0

    with open(filename) as f:
        for line in f:
            cmd, amt = line.split(" ", 1)
            amt = int(amt)
            match cmd:
                case "forward":
                    position += amt
                    depth += aim * amt
                case "backward":
                    position -= amt
                    depth -= aim * amt
                case "down":
                    aim += amt
                case "up":
                    aim -= amt
                case _:
                    print("Panic!")
                    
    # print(f"{filename=} {position=} {depth=}")
    return position * depth

example_file = ".\\02\example-input.txt"
challenge_file = ".\\02\input.txt"
expected_example_product_1 = 15 * 10
expected_example_product_2 = 15 * 60

example_product_1 = get_position_and_depth_product_1(example_file)
challenge_product_1 = get_position_and_depth_product_1(challenge_file)

solution_checker(expected_example_product_1, example_product_1, challenge_product_1)

example_product_2 = get_position_and_depth_product_2(example_file)
challenge_product_2 = get_position_and_depth_product_2(challenge_file)

solution_checker(expected_example_product_2, example_product_2, challenge_product_2)