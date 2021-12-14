from util import Bot
from collections import defaultdict

example_input_file = "./input/14-example.txt" 
challenge_input_file = "./input/14.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    with open(filename) as f:
        polymer_template = f.readline().strip()
        _ = f.readline()
        rules = {}
        ends = [polymer_template[0], polymer_template[-1]]
        for line in f:
            pair, insertion = line.strip().split(" -> ")
            rules[pair] = [pair[0]+insertion, insertion+pair[1]]
        polymer_pairs = defaultdict(int)
        for i in range(len(polymer_template) - 1):
            pair = polymer_template[i:i+2]
            polymer_pairs[pair] += 1
    return polymer_pairs, rules, ends

def polymerise(polymer_pairs, rules):
    new_polymer_pairs = defaultdict(int)
    for pair, count in polymer_pairs.items():
        p1, p2 = rules[pair]
        new_polymer_pairs[p1] += count
        new_polymer_pairs[p2] += count
    return new_polymer_pairs

def difference_after_n_steps(filename, n):
    polymer_pairs, rules, ends = parse_input(filename)
    for _ in range(n):
        polymer_pairs = polymerise(polymer_pairs, rules)
    element_counts = defaultdict(int)
    element_counts[ends[0]] += 1
    element_counts[ends[1]] += 1
    for pair, count in polymer_pairs.items():
        element_counts[pair[0]] += count
        element_counts[pair[1]] += count 
    counts = [count for count in element_counts.values()]
    return (max(counts) - min(counts)) // 2

expected_difference_1 = 1749 - 161
expected_difference_2 = 2192039569602 - 3849876073

bot.check(expected_difference_1, difference_after_n_steps, [10])
bot.check(expected_difference_2, difference_after_n_steps, [40])