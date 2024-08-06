import numpy as np
import pandas as pd
import os
import argparse
from functools import reduce

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        l = f.readlines()[0]
        l = l.replace('\n','')

    return l


def part1(lengths,max_val):

    data = np.arange(max_val+1)
    l = [int(i) for i in lengths.split(',')]

    data, _, _ = round(data,l,0,0)

    print("Part 1: {x}".format(x=data[0]*data[1]))
    return


def round(data,lengths,cur_pos,skip_size):

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

    return data, cur_pos, skip_size


def part2(lengths,max_val):

    lengths = [ord(c) for c in lengths] + [17, 31, 73, 47, 23]
    data = np.arange(max_val+1)
    cur_pos = 0
    skip_size = 0

    for i in range(64):
        data, cur_pos, skip_size = round(data,lengths,cur_pos,skip_size)

    dense_hash = []
    for i in range(16):
        dense_hash.append(reduce(lambda x,y: x^y, data[i*16:(i+1)*16]))

    answer = ''.join('%02x'%i for i in dense_hash)
    print('Part 2: {x}'.format(x=answer))
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\Day10'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--max_val', default=4,type=int)

    args = parser.parse_args()

    lengths = parse_input(os.path.join(args.input_dir,args.file))

    part1(lengths,args.max_val)

    part2(lengths,args.max_val)

