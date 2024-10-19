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
            data.append(int(l))  

    return data


def part1(data,preamble):

    x = preamble
    valid = True
    while valid:
        valid = False
        combos = combinations(data[x-preamble:x],2)
        for (i,j) in combos:
            if data[x] == i + j:
                valid = True
                x += 1
                break

        if not valid:
            print(data[x])
            break               
        
    return x

def part2(data,bad_num):

    for i in range(len(data)):
        sum = data[i]
        j = i+1
        while sum < bad_num:
            sum += data[j]
            j += 1
        if sum == bad_num:
            smallest = min(data[i:j])
            largest = max(data[i:j])
            print(smallest + largest)
            return

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day9'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )
    parser.add_argument('--preamble',default=5,type=int)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    idx = part1(data,args.preamble)

    part2(data[:idx],data[idx])

