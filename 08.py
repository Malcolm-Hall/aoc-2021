from util import solution_checker, Bot 

example_input_file = "./input/08-example.txt" 
challenge_input_file = "./input/08.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    signals = []
    outputs = []
    with open(filename) as f:
        for line in f:
            parsed_line = line.split("|")
            signals.append(parsed_line[0].strip().split(" "))
            outputs.append(parsed_line[1].strip().split(" "))
    
    return signals, outputs

def count_unique(filename):
    _, outputs = parse_input(filename)
    count = 0
    for output in outputs:
        for digit in output:
            l = len(digit)
            if l == 2 or l == 3 or l == 4 or l == 7:
                count += 1
    return count

def overlap(digit, know_digit, num_overlap):
    count_overlap = 0
    for char in digit:
        if char in know_digit:
            count_overlap += 1
    return count_overlap == num_overlap

def match_digit(digit, known_digits):
    l = len(digit)
    if l == 5:
        if overlap(digit, known_digits[7], 3):
            return 3
        elif overlap(digit, known_digits[4], 3):
            return 5
        else:
            return 2
    if l == 6:
        if overlap(digit, known_digits[4], 4):
            return 9
        if overlap(digit, known_digits[1], 2):
            return 0
        else:
            return 6
    return match_unique(digit)
    
def match_unique(digit):
    l = len(digit)
    if l == 2:
        return 1
    if l == 3:
        return 7
    if l == 4:
        return 4
    if l == 7:
        return 8
    return -1   

def sum_output(filename):
    signals, outputs = parse_input(filename)
    output_sum = 0
    for signal, output in zip(signals, outputs):
        digits = signal + output
        known_digits = {}
        for digit in digits:
            known_digits[match_unique(digit)] = digit
        
        decoded_output = ""
        for digit in output:
            decoded_digit = match_digit(digit, known_digits)
            decoded_output += str(decoded_digit)
        output_sum += int(decoded_output)

    return output_sum

expected_count = 26
expected_output_sum = 61229

bot.check(expected_count, count_unique, [])
bot.check(expected_output_sum, sum_output, [])