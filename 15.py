from util import Bot
import math
import copy

example_input_file = "./input/15-example.txt" 
challenge_input_file = "./input/15.txt" 
bot = Bot(example_input_file, challenge_input_file) 

class Node:
    neighbours: list['Node']
    def __init__(self, risk):
        self.risk = risk
        self.visited = False
        self.dist = math.inf
        self.neighbours = []

def parse_input(filename):
    with open(filename) as f:
        nodes = [[Node(int(risk)) for risk in line.strip()] for line in f]
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            nodes[i][j].neighbours = get_neighbours(nodes, i, j)
    nodes[0][0].dist = 0
    return nodes

def get_neighbours(grid, i, j):
    neighbour_offsets = ((-1, 0), ( 0,-1), ( 0, 1), ( 1, 0))
    neighbours = []
    for x, y in neighbour_offsets:
        ni = i + x
        nj = j + y
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
            continue
        neighbours.append(grid[ni][nj])
    return neighbours

def dijkstra(nodes: list[Node], target: Node):
    unvisited_nodes = [node for row in nodes for node in row]

    while len(unvisited_nodes) > 0:
        shortest = None
        for node in unvisited_nodes:
            if shortest is None or node.dist < shortest.dist:
                shortest = node
        unvisited_nodes.remove(shortest)

        if shortest == target:
            return shortest.dist

        for n in shortest.neighbours:
            if n not in unvisited_nodes:
                continue
            new_min = shortest.dist + n.risk
            if new_min < n.dist:
                n.dist = new_min

def total_risk(filename):
    nodes = parse_input(filename)
    total_risk = dijkstra(nodes, nodes[len(nodes)-1][len(nodes[0])-1])
    return total_risk
    
expected_total_risk = 40

bot.check(expected_total_risk, total_risk, [])