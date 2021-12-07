from util import solution_checker, Bot

example_input_file = "./input/02-example.txt"
challenge_input_file = "./input/02.txt"
bot = Bot(example_input_file, challenge_input_file)

def get_position_and_depth_product(filename, move_fn):
    position = 0
    depth = 0
    aim = 0
    with open(filename) as f:
        for line in f:
            cmd, amt = line.split(" ", 1)
            amt = int(amt)
            Dposition, Ddepth, Daim = move_fn(cmd, amt, aim)
            position += Dposition
            depth += Ddepth
            aim += Daim
                    
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

expected_product_1 = 15 * 10
expected_product_2 = 15 * 60

bot.check(expected_product_1, get_position_and_depth_product, [move_1])
bot.check(expected_product_2, get_position_and_depth_product, [move_2])