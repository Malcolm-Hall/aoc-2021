from util import Bot
from queue import PriorityQueue

example_input_file = "./input/15-example.txt" 
challenge_input_file = "./input/15.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def dijkstra(weights, start, end):
    visited = set()
    lowest_weights = {}

    queue = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
        weight_from_start, pos = queue.get()
        if pos == end:
            return weight_from_start

        x, y = pos
        for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if neighbor not in weights or neighbor in visited:
                continue

            new_weight = weight_from_start + weights[neighbor]
            old_weight = lowest_weights.get(neighbor)
            if old_weight and new_weight >= old_weight:
                continue

            lowest_weights[neighbor] = new_weight
            queue.put((new_weight, neighbor))

        visited.add(pos)


def parse_input(filename):
    input_lines = []
    with open(filename) as f:
        for line in f:
            input_lines.append(line.strip())
    
    return len(input_lines), {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input_lines)
        for x, weight in enumerate(line)
    }


def part1(filename):
    size, weights = parse_input(filename)
    e = size - 1
    return dijkstra(weights, start=(0, 0), end=(e, e))


def part2(filename) :
    size, weights = parse_input(filename)
    e = size * 5 - 1
    return dijkstra(
        weights={
            (x + size * i, y + size * j): (weight - 1 + i + j) % 9 + 1
            for i in range(5)
            for j in range(5)
            for (x, y), weight in weights.items()
        },
        start=(0, 0),
        end=(e, e),
    )

expected_total_risk_1 = 40
expected_total_risk_2 = 315

bot.check(expected_total_risk_1, part1, [])
bot.check(expected_total_risk_2, part2, [])