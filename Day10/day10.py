import numpy as np
import pandas as pd
import os
import argparse
from collections import Counter

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

    data.sort()

    jolts = 0
    jump_counter = Counter()

    for adapter in data:
        jump = adapter - jolts
        if jump <= 3:
            jolts = adapter
            jump_counter.update([jump])
        else:
            print('jump too big, did not reach device')
            break

    # add in final jump to your device
    jump_counter.update([3])

    answer = jump_counter[1] * jump_counter[3]
    print(answer)

    return


def part2(data):

    stop = 0
    start = max(data) + 3
    data = np.append(data,start)
    data = np.append(data,stop)
    data.sort()

    temp = list(data)
    paths = {i:0 for i in data}

    paths[start] = 1

    while len(temp) > 0:
        jolt = temp.pop()
        options = data[(data < jolt) & (data >= jolt - 3)]
        for o in options:
            paths[o] += paths[jolt]
    
    print(paths[stop])
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day10'), type=str, help=f'''''')
    parser.add_argument('--file', default='test1.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

