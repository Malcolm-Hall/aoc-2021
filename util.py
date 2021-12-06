
def solution_checker(example_expected, example_result, challenge_result):
    if (example_expected == example_result):
        print("Example passing")
        print(f"Challenge Answer: {challenge_result}")
    else:
        print("Example failing")
        print(f"Expected: {example_expected}, Got: {example_result}")
    print("")

class Bot:
    def __init__(self, example_input_file, challenge_input_file):
        self.example_input_file = example_input_file
        self.challenge_input_file = challenge_input_file
    
    def check(self, expected_example_result, solution_fn, solution_parameters):
        example_result = solution_fn(self.example_input_file, *solution_parameters)
        challenge_result = solution_fn(self.challenge_input_file, *solution_parameters)
        solution_checker(expected_example_result, example_result, challenge_result)