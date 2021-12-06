from util import solution_checker

example_input_file = "./input/04-example.txt"
challenge_input_file = "./input/04.txt"

def parse_input(filename):
    input_boards = []
    with open(filename) as f:
        loc = {}
        exec("call_stack = [" + f.readline() + "]", {}, loc)
        call_stack = loc["call_stack"]
        _ = f.readline()
        lines = f.readlines()
        board_idx = 0
        current_board = []
        for line in lines:
            if board_idx > 4:
                board_idx = 0
                continue
            
            current_line = []
            for i in range(5):
                digits = line[3*i:3*i+3].strip()
                current_line.append(int(digits))
            current_board.append(current_line)
            
            if board_idx > 3:
                input_boards.append(current_board)
                current_board = []
            
            board_idx += 1
    
    return input_boards, call_stack

def get_score(board, call):
    board_sum = 0
    for row in board:
        for number in row:
            if number is not None:
                board_sum += number
    print(f"{board_sum=} {call=}")
    return board_sum * call

def remove_winners(input_boards, call, get_best):
    removals = []
    for board_idx, board in enumerate(input_boards):
            for row in board:
                for no, number in enumerate(row):
                    if number == call:
                        row[no] = None
                        winner = False
                        for row in board:
                            if row.count(None) == 5:
                                winner = True
                                break
                        for i in range(5):
                            column = [board[j][i] for j in range(5)]
                            if column.count(None) == 5:
                                winner = True
                                break
                        if winner:
                            if get_best or len(input_boards) == 1:
                                return get_score(board, call)
                            else:
                                removals.append(board_idx)

    removals = list(dict.fromkeys(removals))
    for idx in reversed(removals):
        input_boards.pop(idx)


def get_final_score(filename, get_best):
    input_boards, call_stack = parse_input(filename)
    for call in call_stack:
        score = remove_winners(input_boards, call, get_best)
        if score is not None:
            return score


expected_example_best_score = 188 * 24
expected_example_worst_score = 148 * 13

example_best_score = get_final_score(example_input_file, True)
challenge_best_score = get_final_score(challenge_input_file, True)

solution_checker(expected_example_best_score, example_best_score, challenge_best_score)

example_worst_score = get_final_score(example_input_file, False)
challenge_worst_score = get_final_score(challenge_input_file, False)

solution_checker(expected_example_worst_score, example_worst_score, challenge_worst_score)