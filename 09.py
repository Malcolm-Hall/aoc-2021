from util import solution_checker, Bot 

example_input_file = "./input/09-example.txt" 
challenge_input_file = "./input/09.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    with open(filename) as f:
        height_map = []
        for line in f:
            row = [int(height) for height in line.strip()]
            height_map.append(row)
    return height_map

def get_neighbours(height_map, i, j):
    neighbours = []
    n_points = []
    if i > 0:
        neighbours.append(height_map[i-1][j])
        n_points.append((i-1, j))
    if i < len(height_map) - 1:
        neighbours.append(height_map[i+1][j])
        n_points.append((i+1, j))
    if j > 0:
        neighbours.append(height_map[i][j-1])
        n_points.append((i, j-1))
    if j < len(height_map[0]) - 1:
        neighbours.append(height_map[i][j+1])
        n_points.append((i, j+1))
    return neighbours, n_points

def is_low_point(height_map, i, j):
    neighbours, _ = get_neighbours(height_map, i, j)
    if min(neighbours) > height_map[i][j]:
        return True
    return False

def sum_risk_levels(filename):
    risk_level_sum = 0
    height_map = parse_input(filename)
    for i, row in enumerate(height_map):
        for j, point in enumerate(row):
            if is_low_point(height_map, i, j):
                risk_level_sum += 1 + point
    return risk_level_sum

def basin_size(queue, visited, height_map):
    while len(queue) > 0:
        i, j = queue.pop(0)
        neighbours, n_points = get_neighbours(height_map, i, j)
        for neighbour, n_point in zip(neighbours, n_points):
            if neighbour == 9 or n_point in visited:
                continue
            visited.add(n_point)
            queue.append(n_point)
    return len(visited)

def basin_product(filename):
    basin_sizes = []
    height_map = parse_input(filename)
    for i, row in enumerate(height_map):
        for j, _ in enumerate(row):
            if is_low_point(height_map, i, j):
                basin_sizes.append(basin_size([(i, j)], {(i, j)}, height_map))
    sorted_basins = sorted(basin_sizes, reverse=True)
    basin_product = 1
    for size in sorted_basins[:3]:
        basin_product *= size
    return basin_product

expected_risk_level_sum = 15
expected_basin_product = 9 * 14 * 9

bot.check(expected_risk_level_sum, sum_risk_levels, [])
bot.check(expected_basin_product, basin_product, [])