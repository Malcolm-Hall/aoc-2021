from util import Bot 

example_input_file = "./input/13-example.txt" 
challenge_input_file = "./input/13.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    with open(filename) as f:
        dots  = set()
        folds = []
        lines = f.readlines()
        fold_cmd_start = None
        for i, line in enumerate(lines):
            if line == "\n":
                fold_cmd_start = i + 1
                break
            loc = {}
            exec("dot = (" + line.strip() + ")", {}, loc)
            dots.add(loc["dot"])
        for line in lines[fold_cmd_start:]:
            fold = line.split(" ")[2].strip().split("=")
            fold[1] = int(fold[1])
            folds.append(fold)
    return dots, folds

def fold_page(dots, fold):
    fold_axis = fold[0]
    fold_line = fold[1]
    new_dots = set()
    for dot in dots:
        x, y = dot
        if fold_axis == "x":
            dx = x - fold_line
            new_dots.add((abs(dx)-1, y))
        elif fold_axis == "y":
            dy = y - fold_line
            new_dots.add((x, fold_line - abs(dy)))
        else:
            raise Exception("Panic!")
    return new_dots

def page_view(dots):
    max_x = max([x for x,_ in dots]) + 1
    max_y = max([y for _,y in dots]) + 1
    dot_map = [[" " for _ in range(max_x)] for _ in range(max_y)]
    for x, y in dots:
        dot_map[y][x] = "#"
    page_view = "\n"
    for line in dot_map:
        page_view += "".join(reversed(line)) + "\n"
    return page_view

def dots_after_one_fold(filename):
    dots, folds = parse_input(filename)
    dots = fold_page(dots, folds[0])
    return len(dots)

def page_view_after_folds(filename):
    dots, folds = parse_input(filename)
    for fold in folds:
        dots = fold_page(dots, fold)
    return page_view(dots)

expected_dots_after_one_fold = 17
expected_page_view_after_folds = (
    '\n'      +
    '#####\n' +
    '#   #\n' +
    '#   #\n' +
    '#   #\n' +
    '#####\n'
)

bot.check(expected_dots_after_one_fold, dots_after_one_fold, [])
bot.check(expected_page_view_after_folds, page_view_after_folds, [])