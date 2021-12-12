from util import solution_checker, Bot 
from collections import defaultdict

example_input_file = "./input/12-example.txt" 
challenge_input_file = "./input/12.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    caves = defaultdict(set)
    with open(filename) as f:
        for line in f:
            a, b = line.strip().split("-")
            caves[a].add(b)
            caves[b].add(a)
    return caves

def count_distinct_paths(filename, can_double_visit=False):
    caves = parse_input(filename)
    return bfs(caves, ("start", ), can_double_visit)

def bfs(caves, visited, can_double_visit=False):
    if visited[-1] == "end":
        return 1
    paths = 0
    for next_cave in caves[visited[-1]]:
        updated_visited = visited + (next_cave, )
        if not (next_cave in visited and next_cave.islower()):
            paths += bfs(caves, updated_visited, can_double_visit)
        elif can_double_visit and visited.count(next_cave) == 1 and next_cave != "start":
            paths += bfs(caves, updated_visited, False)
    return paths

expected_distinct_paths_1 = 226
expected_distinct_paths_2 = 3509

bot.check(expected_distinct_paths_1, count_distinct_paths, [])
bot.check(expected_distinct_paths_2, count_distinct_paths, [True])
