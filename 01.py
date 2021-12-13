from util import Bot

example_input_file = "./input/01-example.txt"
challenge_input_file = "./input/01.txt"
bot = Bot(example_input_file, challenge_input_file)

def tally_depth_increase_1(filename: str) -> int:
    prev = None
    tally = 0

    with open(filename) as f:
        for line in f:
            data = int(line)
            if prev is not None and data > prev:
                tally += 1
            prev = data

    return tally

def tally_depth_increase_2(filename: str) -> int:
    pprev = None
    prev = None
    prev_window_sum = None
    tally = 0

    with open(filename) as f:
        for line in f:
            data = int(line)
            if prev is not None and pprev is not None:
                window_sum = sum([pprev, prev, data])
                if prev_window_sum is not None and window_sum > prev_window_sum:
                    tally += 1
                prev_window_sum = window_sum
            pprev = prev
            prev = data

    return tally

expected_tally_1 = 7
expected_tally_2 = 5

bot.check(expected_tally_1, tally_depth_increase_1, [])
bot.check(expected_tally_2, tally_depth_increase_2, [])
