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

example_file = "example-input.txt"
challenge_file = "input.txt"
expected_example_tally_1 = 7
expected_example_tally_2 = 5

example_tally_1 = tally_depth_increase_1(example_file)
challenge_tally_1 = tally_depth_increase_1(challenge_file)

if (example_tally_1 == expected_example_tally_1):
    print("Example 1 passing")
    print(f"Challenge 1 Answer: {challenge_tally_1}")
else:
    print("Example 1 failing")
    print(f"Expected: {expected_example_tally_1}, Got: {example_tally_1}")

example_tally_2 = tally_depth_increase_2(example_file)
challenge_tally_2 = tally_depth_increase_2(challenge_file)

if (example_tally_2 == expected_example_tally_2):
    print("Example 2 passing")
    print(f"Challenge 2 Answer: {challenge_tally_2}")
else:
    print("Example 2 failing")
    print(f"Expected: {expected_example_tally_2}, Got: {example_tally_2}")
