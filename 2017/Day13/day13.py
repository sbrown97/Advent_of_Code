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
            l = l.split(': ')
            row = tuple(int(x) for x in l)
            data.append(row)  

    return data


def part1(data):

    penalty = 0
    for (d, r) in data:
        if d % ((r * 2) - 2) == 0:
            penalty += d * r

    print(f'Part 1: {penalty}')
    return

def part2(data):

    success = False
    delay = 0

    while not success:
        delay += 1
        caught = False
        for (d,r) in data:
            if (d + delay) % ((r * 2) - 2) == 0:
                caught = True
                break

        success = not caught
        
    print(f'Part 2: {delay}')

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\\Day13'), type=str)
    parser.add_argument('--file', default='input.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

