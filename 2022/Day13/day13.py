import numpy as np
import os
import argparse
from copy import deepcopy
from functools import cmp_to_key

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    temp = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')

            if l == '':
                continue
            else:
                l = eval(l)
                data.append(l)

    return data


def compare(l,r):

    left = deepcopy(l)
    right = deepcopy(r)
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif type(right) == int:
        return compare(left,[right])
    elif type(left) == int:
        return compare([left],right)
    elif type(left) == list and type(right) == list:
        while left:
            if right:
                val = compare(left.pop(0),right.pop(0))
                if val != 0:
                    return val
            else:
                return 1
        if right:
            return -1
        else:
            return 0
    return

def part1(data):
    
    pairs = deepcopy(data)
    assessment = []
    for i in range(0,len(pairs),2):
        left = pairs[i]
        right = pairs[i+1]
        assessment.append(compare(left,right))

    right = np.where(np.array(assessment) == -1)
    right = [i + 1 for i in list(right[0])]
    print(sum(right))

    return

def part2(data):

    data.append([[2]])
    data.append([[6]])

    sorted_data = sorted(data, key=cmp_to_key(compare))

    decoder1 = sorted_data.index([[2]]) + 1
    decoder2 = sorted_data.index([[6]]) + 1

    print(decoder1 * decoder2)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\\Day13'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

