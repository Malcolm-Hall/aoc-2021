from util import Bot
from io import StringIO
from math import prod

example_input_file = "./input/16-example.txt" 
challenge_input_file = "./input/16.txt" 
bot = Bot(example_input_file, challenge_input_file) 

def parse_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())
    return data

class Packet:
    def __init__(self, hex_input=None, bin_input=None, stream=None):
        if not (hex_input or bin_input or stream):
            raise TypeError('No input provided')
        if hex_input:
            bin_input = ''.join(f'{int(char, 16):04b}' for char in hex_input)
        if bin_input:
            stream = StringIO(bin_input)
        self.stream = stream
        self.version = int(self.stream.read(3), 2)
        self.type_id= int(self.stream.read(3), 2)
        self.subpackets = [] if self.type_id == 4 else self.read_subpackets()
        self.value = {
            0: self.sum,
            1: self.prod,
            2: self.min,
            3: self.max,
            4: self.read_literal,
            5: self.greater_than,
            6: self.less_than,
            7: self.equal
        }[self.type_id]()
        self.versions_sum = sum(self.versions())

    def read_literal(self):
        heading = literal = ''
        while heading != '0':
            heading = self.stream.read(1)
            literal += self.stream.read(4)
        return int(literal, 2)

    def read_subpackets(self):
        length_type_id = self.stream.read(1)
        if length_type_id == '0':
            total_length = int(self.stream.read(15), 2)
            end = self.stream.tell() + total_length
            subpackets = []
            while self.stream.tell() < end:
                subpackets.append(Packet(stream=self.stream))
        else:
            num_subpackets = int(self.stream.read(11), 2)
            subpackets = [Packet(stream=self.stream) for _ in range(num_subpackets)]
        return subpackets 

    def sum(self):
        return sum(subpacket.value for subpacket in self.subpackets)

    def prod(self):
        return prod(subpacket.value for subpacket in self.subpackets)

    def min(self):
        return min(subpacket.value for subpacket in self.subpackets)

    def max(self):
        return max(subpacket.value for subpacket in self.subpackets)

    def greater_than(self):
        first, second, *_ = self.subpackets
        return int(first.value > second.value)

    def less_than(self):
        first, second, *_ = self.subpackets
        return int(first.value < second.value)

    def equal(self):
        first, second, *_ = self.subpackets
        return int(first.value == second.value)
                
    def versions(self):
        yield self.version
        for subpacket in self.subpackets:
            yield from subpacket.versions()
    
    def __repr__(self):
        return f'Packet(version={self.version}, type_id={self.type_id}, value={self.value}, subpackets={self.subpackets})'


def read_packet(filename, packet_index):
    data = parse_input(filename)
    packet = Packet(data[packet_index])
    return packet

def version_number_sum(filename, packet_index=0):
    packet = read_packet(filename, packet_index)
    return packet.versions_sum

def content_result(filename, packet_index=0):
    packet = read_packet(filename, packet_index)
    return packet.value

expected_version_number_sums = (6, 9, 14, 16, 12, 23, 31)
expected_content_results = (3, 54, 7, 9, 1, 0, 0, 1)

for i, expected_version_sum in enumerate(expected_version_number_sums):
    if not bot.check_example(expected_version_sum, version_number_sum, [i]):
        exit(1)
print(version_number_sum(challenge_input_file))

for j, expected_result in enumerate(expected_content_results):
    if not bot.check_example(expected_result, content_result, [len(expected_version_number_sums) + j]):
        exit(1)
print(content_result(challenge_input_file))

