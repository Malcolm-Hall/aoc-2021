import os, sys

Day = str

def format_day(number: int) -> Day:
    if number > 0 and number < 10:
        return "0" + str(number)
    elif number < 26:
        return str(number)
    raise Exception("'Bouta Explode")

def make_file(path, contents: str = ""):
    dir = os.path.dirname(path)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(contents)

def make_source_and_input_file(day: Day, src_suffix: str = ".py", input_suffix: str = ".txt"):
    challenge_input_path = f"./input/{day}{input_suffix}"
    example_input_path = f"./input/{day}-example{input_suffix}"
    src_path = f"./{day}{src_suffix}"
    src_contents = ""
    if src_suffix == ".py":
        src_contents = (
            "from util import Bot \n"
            "\n"
            f"example_input_file = \"{example_input_path}\" \n"
            f"challenge_input_file = \"{challenge_input_path}\" \n"
            "bot = Bot(example_input_file, challenge_input_file) \n"
        )
    make_file(challenge_input_path)
    make_file(example_input_path)
    make_file(src_path, src_contents)

def make_instruction_file(day: Day, suffix: str = ".txt"):
    instruction_path = f"./instructions/{day}{suffix}"
    make_file(instruction_path)

def make_template(from_day: int = 1, to_day: int = 25, src_suffix: str = ".py", input_suffix: str = ".txt"):
    util_file = "./util.py"
    make_file(util_file)
    for i in range(from_day, to_day + 1):
        day = format_day(i)
        make_source_and_input_file(day, src_suffix, input_suffix)
        make_instruction_file(day, input_suffix)

def parse_argv():
    kwargs = {
        "_": "_",
        "from_day": 1, 
        "to_day": 25, 
        "src_suffix": ".py", 
        "input_suffix": ".txt"
    }
    for key, arg in zip(kwargs.keys(), sys.argv):
        parsed_arg = arg
        if type(kwargs[key]) is int:
            parsed_arg = int(arg)
        kwargs[key] = parsed_arg
    kwargs.pop("_")
    return kwargs

if __name__ == '__main__':
    kwargs = parse_argv()
    make_template(**kwargs)