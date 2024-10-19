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
            data.append(int(l))  

    return np.array(data)


def part1(data):

    return sum(np.floor(data/3) - 2)

def part2(data):

    fuel = [max(0,np.floor(x/3)-2) for x in data]
    total = sum(fuel)
    while sum(fuel) > 0:
        fuel = [max(0,np.floor(x/3)-2) for x in fuel]
        total += sum(fuel)

    print(total)
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019/Day1'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    print(part1(data))

    part2(data)

