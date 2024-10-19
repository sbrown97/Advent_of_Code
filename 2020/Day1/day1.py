import numpy as np
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
            data.append(int(l))  

    return np.array(data)

def do_math(data,n,total):
    for combo in combinations(data,n):
        if sum(combo) == total:
            print(np.prod(combo))
            return


def part1(data):

    do_math(data,2,2020) 
            
    return 


def part2(data):

    do_math(data,3,2020)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day1'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

