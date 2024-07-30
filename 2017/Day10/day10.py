import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        l = f.readlines()[0]
        l = l.replace('\n','').split(',')
        lengths = [int(x) for x in l]  

    return lengths


def part1(lengths,max_val):

    cur_pos = 0
    skip_size = 0
    data = np.arange(max_val+1)

    for l in lengths:
        # get sublist to reverse
        subset = data.take(range(cur_pos,cur_pos+l),mode='wrap')
        subset = list(subset)
        # replace in data
        for i in range(cur_pos,cur_pos+l):
            i = i % len(data)
            data[i] = subset.pop()

        cur_pos += l + skip_size
        cur_pos %= len(data)
        skip_size += 1

    print("Part 1: {x}".format(x=data[0]*data[1]))
    return

def part2(lengths):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\Day10'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--max_val', default=5,type=int)

    args = parser.parse_args()

    lengths = parse_input(os.path.join(args.input_dir,args.file))

    part1(lengths,args.max_val)

    part2(lengths)

