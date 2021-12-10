from util import solution_checker, Bot 

example_input_file = "./input/10-example.txt" 
challenge_input_file = "./input/10.txt" 
bot = Bot(example_input_file, challenge_input_file) 

BRACKETS = {
    '(' : ')', 
    '[' : ']', 
    '{' : '}', 
    '<' : '>',
}

ERROR_SCORE = {
    None : 0,
    ')' : 3, 
    ']' : 57, 
    '}' : 1197, 
    '>' : 25137,
}

AUTOCOMPLETE_SCORE = {
    None : 0,
    ')' : 1, 
    ']' : 2, 
    '}' : 3, 
    '>' : 4,
}

def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def brackets_match(opening, closing):
    return BRACKETS[opening] == closing

def check_syntax(line):
    stack = []
    for bracket in line:
        if bracket in BRACKETS.keys():
            stack.append(bracket)
        else:
            opening_bracket = stack.pop()
            if not brackets_match(opening_bracket, bracket):
                return bracket, stack
    return None, stack

def syntax_error_score(filename):
    input = parse_input(filename)
    score = 0
    for line in input:
        illegal_bracket, _ = check_syntax(line)
        score += ERROR_SCORE[illegal_bracket]
    return score

def stack_score(stack):
    stack_score = 0
    for bracket in reversed(stack):
        closing_bracket = BRACKETS[bracket]
        stack_score *= 5
        stack_score += AUTOCOMPLETE_SCORE[closing_bracket]
    return stack_score

def autocomplete_score(filename):
    input = parse_input(filename)
    stack_scores = []
    for line in input:
        illegal_bracket, stack = check_syntax(line)
        if illegal_bracket is not None:
            continue
        stack_scores.append(stack_score(stack))
    sorted_stack_scores = sorted(stack_scores)
    return sorted_stack_scores[len(sorted_stack_scores) // 2]


expected_syntax_error_score = 2 * 3 + 57 + 1197 + 25137
expected_autocomplete_score = 288957

bot.check(expected_syntax_error_score, syntax_error_score, [])
bot.check(expected_autocomplete_score, autocomplete_score, [])