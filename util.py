
def solution_checker(example_expected, example_result, challenge_result):
    if (example_expected == example_result):
        print("Example passing")
        print(f"Challenge Answer: {challenge_result}")
    else:
        print("Example failing")
        print(f"Expected: {example_expected}, Got: {example_result}")
    print("")