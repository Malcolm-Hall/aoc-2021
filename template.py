import os, sys

Day = str

def format_day(number: int) -> Day:
    if number > 0 and number < 10:
        return "0" + str(number)
    elif number < 26:
        return str(number)
    raise Exception("'Bouta Explode")

def make_file(path):
    dir = os.path.dirname(path)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    if not os.path.isfile(path):
        with open(path, 'w'):
            pass

def make_source_file(day: Day, suffix: str = ".py"):
    src_path = f"./{day}{suffix}"
    make_file(src_path)

def make_input_files(day: Day, suffix: str = ".txt"):
    base_path = f"./input/{day}"
    challenge_input_path = base_path + suffix
    example_input_path = base_path + "-example" + suffix
    make_file(challenge_input_path)
    make_file(example_input_path)

def make_template(from_day: int = 1, to_day: int = 25, src_suffix: str = ".py", input_suffix: str = ".txt"):
    for i in range(from_day, to_day + 1):
        day = format_day(i)
        make_source_file(day, src_suffix)
        make_input_files(day, input_suffix)

if __name__ == '__main__':
    argv = sys.argv
    kwarg_map = {
        "_": "_",
        "from_day": 1, 
        "to_day": 25, 
        "src_suffix": ".py", 
        "input_suffix": ".txt"
    }
    for i, [key, arg] in enumerate(zip(kwarg_map.keys(), argv)):
        parsed_arg = arg
        if i == 0:
            continue
        elif i <= 2:
            parsed_arg = int(arg)
        kwarg_map[key] = parsed_arg
    kwarg_map.pop("_")
    make_template(**kwarg_map)