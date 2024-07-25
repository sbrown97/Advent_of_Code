import numpy as np
import pandas as pd
import os
import argparse
from itertools import combinations

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            words = l.split(' ')
            data.append(words)  

    return data


def part1(data):

    count_valid = 0
    for passphrase in data:
        if len(passphrase) == len(set(passphrase)):
            count_valid += 1

    print('Part 1: {x}'.format(x=count_valid))

    return

def part2(data):

    count_valid = 0
    for passphrase in data:
        combos = combinations(passphrase,2)
        num_combos = sum(1 for i in combos)
        valid_combos = 0
        for w1, w2 in combinations(passphrase,2):
            if sorted(w1) == sorted(w2):
                break
            else:
                valid_combos += 1
        if valid_combos == num_combos:
            count_valid += 1    

    print("Part 2: {x}".format(x=count_valid))
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\Day4'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

