import sys
sys.path.append("/home/malcolm/Projects/aoc-2021")
from util import solution_checker

def best_final_score(filename):
    input_boards = []
    with open(filename) as f:
        call_stack = f.readline()
        print(call_stack)
        _ = f.readline()
        lines = f.readlines()
        board_idx = 0
        current_board = []
        for line in lines:
            if board_idx > 4:
                board_idx = 0
                continue
            
            if len(line) > 14:
                current_board.append(line[:-1])
            else:
                current_board.append(line)

            if board_idx > 3:
                input_boards.append(current_board)
                current_board = []
            
            board_idx += 1

    # Do something with the input boards

expected_example_score = 188 * 24
example_score = best_final_score("./04/example-input.txt")

solution_checker(expected_example_score, example_score, 0)