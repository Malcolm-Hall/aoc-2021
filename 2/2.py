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
                    
    print(f"{filename=} {position=} {depth=}")
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
                    
    print(f"{filename=} {position=} {depth=}")
    return position * depth

example_file = "example-input.txt"
challenge_file = "input.txt"
expected_example_product_1 = 15 * 10
expected_example_product_2 = 15 * 60

example_product_1 = get_position_and_depth_product_1(example_file)
challenge_product_1 = get_position_and_depth_product_1(challenge_file)

if (example_product_1 == expected_example_product_1):
    print("Example 1 passing")
    print(f"Challenge 1 Answer: {challenge_product_1}")
else:
    print("Example 1 failing")
    print(f"Expected: {expected_example_product_1}, Got: {example_product_1}")

example_product_2 = get_position_and_depth_product_2(example_file)
challenge_product_2 = get_position_and_depth_product_2(challenge_file)

if (example_product_2 == expected_example_product_2):
    print("Example 2 passing")
    print(f"Challenge 2 Answer: {challenge_product_2}")
else:
    print("Example 2 failing")
    print(f"Expected: {expected_example_product_2}, Got: {example_product_2}")