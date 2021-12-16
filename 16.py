from util import Bot
import functools

example_input_file = "./input/16-example.txt" 
challenge_input_file = "./input/16.txt" 
bot = Bot(example_input_file, challenge_input_file) 

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
def parse_input(filename):
    with open(filename) as f:
        packets = []
        for line in f:
            hex_packet = line.strip()
            bin_packet = "".join([hex_to_bin[digit] for digit in hex_packet])
            packets.append(bin_packet)
        return packets

def parse_header(packet):
    version = packet[:3]
    type_id = packet[3:6]
    rest = packet[6:]
    return version, type_id, rest

def parse_100(rest):
    content = ''
    while rest[0] == '1':
        content += rest[:5]
        rest = rest[5:]
    content += rest[:5]
    rest = rest[5:]
    return rest, int(content,2)


def parse_subpackets(rest):
    version_sum = 0
    length_id = rest[0]
    rest = rest[1:]
    contents = []
    if length_id == "0":
        length = rest[:15]
        rest = rest[15:]
        target = int(length, 2)
        while target > 0:
            len_before = len(rest)
            rest, vs, content = decode_packet(rest)
            version_sum += vs
            contents.append(content)
            target -= len_before - len(rest)
    else:
        length = rest[:11]
        rest = rest[11:]
        for _ in range(int(length, 2)):
            rest, vs, content = decode_packet(rest)
            version_sum += vs
            contents.append(content)
    return rest, version_sum, contents

def decode_packet(packet):
    version, type_id, rest = parse_header(packet)
    version_sum = int(version, 2)
    if type_id == '100':
        rest, content = parse_100(rest)
        return rest, version_sum, content
    else:
        rest, vs, contents = parse_subpackets(rest)
        version_sum += vs
    
    match type_id:
        case '000':
            content = sum(contents)
        case '001':
            content = functools.reduce(lambda a, b : a*b, contents)
        case '010':
            content = min(contents)
        case '011':
            content = max(contents)
        case '101':
            content = int(contents[0] > contents[1])
        case '110':
            content = int(contents[0] < contents[1])
        case '111':
            content = int(contents[0] == contents[1])
    
    return rest, version_sum, content
    

def version_number_sum(_, packet):
    _, version_sum, _ = decode_packet(packet)
    return version_sum

def content_result(_, packet):
    _, _, content = decode_packet(packet)
    return content

expected_version_number_sums = (6, 9, 14, 16, 12, 23, 31)
expected_content_results = (3, 54, 7, 9, 1, 0, 0, 1)


example_packets = parse_input(example_input_file)
[challenge_packet] = parse_input(challenge_input_file)

for i, expected_version_sum in enumerate(expected_version_number_sums):
    bot.check_example(expected_version_sum, version_number_sum, [example_packets[i]])

for j, expected_result in enumerate(expected_content_results):
    bot.check_example(expected_result, content_result, [example_packets[len(expected_version_number_sums) + j]])

# print(version_number_sum(None, challenge_packet))
print(content_result(None, challenge_packet))