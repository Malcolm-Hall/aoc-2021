import os
import shutil

Day = str

def format_day(number: int) -> Day:
    if number > 0 and number < 10:
        return "0" + str(number)
    elif number < 26:
        return str(number)
    raise Exception("'Bouta Explode")

def make_file(path):
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




day07 = format_day(7)
make_source_file(day07)