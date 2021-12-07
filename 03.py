from util import solution_checker, Bot

example_input_file = "./input/03-example.txt"
challenge_input_file = "./input/03.txt"
bot = Bot(example_input_file, challenge_input_file)

def parse_input(filename):
    input = []
    with open(filename) as f:
        for line in f:
            input.append([char for char in line if char != '\n'])
    return input

def parse_to_decimal(bin_array):
    bin_str = '0b'
    for char in bin_array:
        bin_str += char
    return int(bin_str, 2)

def get_zeros_and_ones(input, i):
    zeros = []
    ones = []
    for line in input:
        if line[i] == '0':
            zeros.append(line)
        elif line[i] == '1':
            ones.append(line)
    return zeros, ones

def power_consumption(filename):
    input = parse_input(filename)
    gamma = []
    epsilon = []
    
    for i in range(len(input[0])):
        zeros, ones = get_zeros_and_ones(input, i)
        
        if len(zeros) > len(ones):
            gamma.append('0')
            epsilon.append('1')
        elif len(ones) > len(zeros):
            gamma.append('1')
            epsilon.append('0')
        else:
            raise Exception("Panic!")
    
    gamma_value = parse_to_decimal(gamma)
    epsilon_value = parse_to_decimal(epsilon)
    return gamma_value * epsilon_value

def life_support_rating(filename):
    input = parse_input(filename)
    
    def search(input, breaker):
        tree = input
        for i in range(len(tree[0])):
            zeros, ones = get_zeros_and_ones(tree, i)

            if breaker == '0':
                gt_case = ones
                lte_case = zeros
            elif breaker == '1':
                gt_case = zeros
                lte_case = ones
            else:
                raise Exception("Panic!")

            if len(zeros) > len(ones):
                tree = gt_case
            elif len(zeros) <= len(ones):
                tree = lte_case
            
            if len(tree) == 1:
                break

        return parse_to_decimal(tree[0])

    oxy_rating = search(input, '1')
    co2_rating = search(input, '0')
    return oxy_rating * co2_rating

expected_power = 22 * 9
expected_rating = 23 * 10

bot.check(expected_power, power_consumption, [])
bot.check(expected_rating, life_support_rating, [])