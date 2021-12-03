import sys
sys.path.append("C:\\dev\\aoc-2021")
from util import solution_checker

def power_consumption(filename):
    input = []
    gamma = []
    epsilon = []
    with open(filename) as f:
        for line in f:
            input.append([char for char in line if char != '\n'])
    
    for i in range(len(input[0])):
        zero = 0
        one = 0
        for line in input:
            if line[i] == '0':
                zero += 1
            elif line[i] == '1':
                one += 1
        
        if zero > one:
            gamma.append('0')
            epsilon.append('1')
        elif one > zero:
            gamma.append('1')
            epsilon.append('0')
        else:
            raise Exception("Panic!")
    
    gamma_bin = '0b'
    epsilon_bin = '0b'
    for gbit, ebit in zip(gamma, epsilon):
        gamma_bin += gbit
        epsilon_bin += ebit

    return int(gamma_bin, 2) * int(epsilon_bin, 2)

def life_support_rating(filename):
    input = []
    with open(filename) as f:
        for line in f:
            input.append([char for char in line if char != '\n'])
    
    def search(input, breaker):
        tree = input
        i = 0
        while len(tree) > 1:
            zero = 0
            one = 0
            zeros = []
            ones = []
            for line in tree:
                if line[i] == '0':
                    zero += 1
                    zeros.append(line)
                elif line[i] == '1':
                    one += 1
                    ones.append(line)
            i += 1

            if breaker == '0':
                if len(zeros) > len(ones):
                    tree = ones
                elif len(zeros) < len(ones):
                    tree = zeros
                else:
                    tree = zeros
            elif breaker == '1':
                if len(zeros) > len(ones):
                    tree = zeros
                elif len(zeros) < len(ones):
                    tree = ones
                else:
                    tree = ones
            else:
                raise Exception("Panic!")

        output_bin = '0b'
        for char in tree[0]:
            output_bin += char

        return int(output_bin, 2)

    oxy_rating = search(input, '1')
    co2_rating = search(input, '0')
    return oxy_rating * co2_rating
        
        

example_file = ".\\03\example-input.txt"
challenge_file = ".\\03\input.txt"
expected_example_power = 22 * 9
expected_example_rating = 23 * 10

example_power = power_consumption(example_file)
challenge_power = power_consumption(challenge_file)

solution_checker(expected_example_power, example_power, challenge_power)

example_rating = life_support_rating(example_file)
challenge_rating = life_support_rating(challenge_file)

solution_checker(expected_example_rating, example_rating, challenge_rating)