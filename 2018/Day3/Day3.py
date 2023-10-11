import numpy as np
import pandas as pd
import os
import argparse
from itertools import product
from collections import Counter


def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = pd.DataFrame(columns=['claim','left','top','width','height'])

    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(" ")
            claim = l[0]
            [left,top] = l[2].split(',')
            top = top.replace(":","")
            [width,height] = l[3].split("x")
            row = [x for x in l]
            data = data.append({'claim':claim,
                                'left':int(left),
                                'top':int(top),
                                'width':int(width),
                                'height':int(height)},
                                ignore_index=True)  

    return data


def makeSet(row):
    return list(product(range(row.top, row.top + row.height), range(row.left, row.left + row.width)))


def part1(data):

    data['squares'] = data.apply(makeSet,axis=1)

    square_counter = Counter()

    for idx, row in data.iterrows():
        square_counter.update(row.squares)
    
    overlap = set([key for key in square_counter if square_counter[key] > 1])

    print("Part 1: {x}".format(x=len(overlap)))

    return overlap

def part2(data, overlap):

    for idx, row in data.iterrows():
       intersect = set(row.squares).intersection(overlap)
       if len(intersect) == 0:
           print("Part 2: claim {c}".format(c=row.claim))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day3'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    overlap = part1(data)

    part2(data, overlap)

