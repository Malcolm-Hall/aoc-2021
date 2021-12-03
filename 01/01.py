import sys
sys.path.append("C:\\dev\\aoc-2021")
from util import solution_checker 

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

example_file = ".\\01\example-input.txt"
challenge_file = ".\\01\input.txt"
expected_example_tally_1 = 7
expected_example_tally_2 = 5

example_tally_1 = tally_depth_increase_1(example_file)
challenge_tally_1 = tally_depth_increase_1(challenge_file)

solution_checker(expected_example_tally_1, example_tally_1, challenge_tally_1)

example_tally_2 = tally_depth_increase_2(example_file)
challenge_tally_2 = tally_depth_increase_2(challenge_file)

solution_checker(expected_example_tally_2, example_tally_2, challenge_tally_2)
