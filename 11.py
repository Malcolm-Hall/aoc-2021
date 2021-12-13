from util import Bot 

example_input_file = "./input/11-example.txt" 
challenge_input_file = "./input/11.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    with open(filename) as f:
        input = [[int(level) for level in line.strip()] for line in f]
    return input

def get_neighbours(grid, i, j):
    neighbour_offsets = (
        (-1,-1), (-1, 0), (-1, 1),
        ( 0,-1)     ,     ( 0, 1),
        ( 1,-1), ( 1, 0), ( 1, 1),
    )
    neighbour_indices = []
    for x, y in neighbour_offsets:
        ni = i + x
        nj = j + y
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
            continue
        neighbour_indices.append((ni, nj))
    return neighbour_indices

def flash_and_update(grid, flash_accumulator=0):
    update_queue = []
    for i, row in enumerate(grid):
        for j, level in enumerate(row):
            if level > 9:
                grid[i][j] = -1
                flash_accumulator += 1
                update_queue.extend(get_neighbours(grid, i, j))
    
    flash_again = False
    for ni, nj in update_queue:
        if grid[ni][nj] == -1:
            continue
        grid[ni][nj] += 1
        if grid[ni][nj] > 9:
            flash_again = True

    if flash_again:
        return flash_and_update(grid, flash_accumulator)
    
    return grid, flash_accumulator

def step_grid(grid):
    grid = [[level + 1 if level > 0 else 1 for level in row] for row in grid]
    grid, num_flashes = flash_and_update(grid)
    return grid, num_flashes

def simultaneous_flash(grid):
    for row in grid:
        for level in row:
            if level != -1:
                return False
    return True

def count_flashes(filename, n):
    input = parse_input(filename)
    total_flashes = 0
    grid = input
    for i in range(n):
        grid, num_flashes = step_grid(grid)
        total_flashes += num_flashes
    return total_flashes

def steps_until_simultaneous_flash(filename):
    input = parse_input(filename)
    grid = input
    num_steps = 0
    while not simultaneous_flash(grid):
        grid, _ = step_grid(grid)
        num_steps += 1
    return num_steps

expected_number_of_flashes = 1656
expected_steps_until_simultaneous_flash = 195

bot.check(expected_number_of_flashes, count_flashes, [100])
bot.check(expected_steps_until_simultaneous_flash, steps_until_simultaneous_flash, [])