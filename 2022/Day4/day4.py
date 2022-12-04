import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(',')

            row = [(int(x.split('-')[0]),int(x.split('-')[1])) for x in l]
            data.append(row)  

    return data


def part1(data):

    containedPairs = 0

    for pair in data:
        elf1 = set(range(pair[0][0],pair[0][1]+1))
        elf2 = set(range(pair[1][0],pair[1][1]+1))
        common = elf1.intersection(elf2)
        if (common == elf1) | (common == elf2):
            containedPairs += 1

    print(containedPairs)     

    return

def part2(data):

    overlapping = 0

    for pair in data:
        elf1 = set(range(pair[0][0],pair[0][1]+1))
        elf2 = set(range(pair[1][0],pair[1][1]+1))
        common = elf1.intersection(elf2)
        if common:
            overlapping += 1

    print(overlapping)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day4'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

