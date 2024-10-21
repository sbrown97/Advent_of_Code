import os
import argparse
import operator
from collections import defaultdict

ops = {
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    'inc': operator.add,
    'dec': operator.sub
}

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row = l.split(' ')

            data.append(row)  

    return data


def part1(data):

    registers = defaultdict(int)
    max_val = 0

    for instruction in data:
        if ops[instruction[5]](int(registers[instruction[4]]),int(instruction[6])):
            registers[instruction[0]] = ops[instruction[1]](int(registers[instruction[0]]),int(instruction[2]))
            if registers[instruction[0]] > max_val:
                max_val = registers[instruction[0]]

    print(f'Part 1: {max(registers.values())}')
    print(f'Part 2: {max_val}')
    return

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\\Day8'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

