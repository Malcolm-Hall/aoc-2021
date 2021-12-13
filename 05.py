from util import Bot

example_input_file = "./input/05-example.txt"
challenge_input_file = "./input/05.txt"
bot = Bot(example_input_file, challenge_input_file)

class Counter(dict):
    def __missing__(self, key):
        return 0

def sign(number):
    if number == 0:
        return 0
    return int(number/abs(number))

def number_of_dangerous_points(filename, diagonals=False):
    overlap = Counter()
    with open(filename) as f:
        for line in f:
            bits = line.split(" ") # [point_1, "->", point_2]
            loc = {}
            exec(f"start = ({bits[0]}) \nend = ({bits[2]})", {}, loc)
            start_x, start_y = loc["start"]
            end_x, end_y = loc["end"]
            x = start_x
            y = start_y
            DY = (end_y - start_y)
            DX = (end_x - start_x)
            if DX != 0 and DY != 0 and not diagonals:
                continue
            line_length = max(abs(DY), abs(DX)) + 1
            dx = sign(DX)
            dy = sign(DY)
            i = 0
            while i < line_length:
                overlap[(x,y)] += 1
                x += dx
                y += dy
                i += 1

    dangerous_points = 0
    for value in overlap.values():
        if value > 1:
            dangerous_points += 1
    return dangerous_points

expected_dangerous_points_1 = 5
expected_dangerous_points_2 = 12

bot.check(expected_dangerous_points_1, number_of_dangerous_points, [])
bot.check(expected_dangerous_points_2, number_of_dangerous_points, [True])