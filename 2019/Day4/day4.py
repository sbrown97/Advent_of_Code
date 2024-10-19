import numpy as np
from collections import Counter
import os
import argparse

def part1(data):

    num_passwords = 0
    min_digit1 = int(np.floor(data[0]/100000))
    for digit1 in range(min_digit1,10):
        for digit2 in range(digit1,10):
            for digit3 in range(digit2,10):
                for digit4 in range(digit3,10):
                    for digit5 in range(digit4,10):
                        for digit6 in range(digit5,10):
                            num = int(str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(digit5) + str(digit6))
                            
                            # must be in range
                            if (num >= data[0]) & (num <= data[1]):
                                # must be 2 adjacent identical digits
                                if (digit1 == digit2) | (digit2 == digit3) | (digit3 == digit4) | (digit4 == digit5) | (digit5 == digit6):
                                    num_passwords += 1
    print('Part 1: ',num_passwords)
    return

def part2(data):
 
    num_passwords = 0
    min_digit1 = int(np.floor(data[0]/100000))
    for digit1 in range(min_digit1,10):
        for digit2 in range(digit1,10):
            for digit3 in range(digit2,10):
                for digit4 in range(digit3,10):
                    for digit5 in range(digit4,10):
                        for digit6 in range(digit5,10):
                            num = int(str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(digit5) + str(digit6))
                            
                            # must be in range
                            if (num >= data[0]) & (num <= data[1]):
                                # must be 2 adjacent identical digits
                                # because of strictly increasing rule, if there are 2 identical digits, they must be adjacent
                                digit_count = Counter(str(num))

                                if 2 in digit_count.values():
                                    num_passwords += 1
    print('Part 2: ', num_passwords)
    
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day4'), type=str )
    parser.add_argument('--range', default='172930-683082',type=str )

    args = parser.parse_args()

    data = args.range.split('-')
    data = [int(x) for x in data]

    part1(data)

    part2(data)

