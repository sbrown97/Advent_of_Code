import string
import os
import argparse
import re

def part1(path):
    """ read in and parse input data
    returns """

    start = r'4920414d2054574f20464f4f4c53'
    stop = r'444945204e4f542c20504f4f52204445415448'
    pattern = start + r"(.*?)" + stop

    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        
        with open(file_path,'r') as f:
            data = f.read()
            if (start in data) and (stop in data):
                match = re.search(pattern,data)
                if match:
                    payload = match.group(1)
                    print(f'part 1: {payload.count('a')}')

    return 



def part2(path):

    with open(path, 'r') as f:
        data = f.read()
        data = data.split(' ')
        data = [''.join(['1' if i == '0' else '0' for i in x]) + '0' for x in data]
        data = [int(x,2) for x in data]
        print(f'part2: {sum(data)}')

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Cyber TMYC/week2/part1_inputs'), type=str)
    parser.add_argument('--part2', default='Cyber TMYC/week2/Problem 2 Keyfile.txt',type=str)

    args = parser.parse_args()

    part1(args.input_dir)

    part2(args.part2)

