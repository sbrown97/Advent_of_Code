import numpy as np
import pandas as pd
import os
import argparse
from itertools import product
from collections import Counter


def parse_input(path):
    """ read in and parse input data
    returns DataFrame with one row per claim"""
    
    data = pd.DataFrame(columns=['claim','left','top','width','height'])

    with open(path) as f:
        for l in f:
            # split string to get claim id, distance from left, distance from top, width, and height
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
    """
    returns the set of (y,x) squares described by the claim defined in row data
    """
    return set(product(range(row.top, row.top + row.height), range(row.left, row.left + row.width)))


def part1(data):
    """
    Count the number of squares that appear in more than 1 claim
    """
    
    # get the set of squares covered by each claim
    data['squares'] = data.apply(makeSet,axis=1)

    # count the number of occurances of each square accross claims
    square_counter = Counter()
    for idx, row in data.iterrows():
        square_counter.update(row.squares)
    
    # overlap is any square with a count greater than 1
    overlap = set([key for key in square_counter if square_counter[key] > 1])

    print("Part 1: {x}".format(x=len(overlap)))

    return overlap

def part2(data, overlap):
    """
    Find the claim that doesn't overlap any other claim
    """

    # check each claim
    for idx, row in data.iterrows():
       # if none of the claim's squares appear in the overalp set, then it doesn't overlap any other claim
       intersect = row.squares.intersection(overlap)
       if len(intersect) == 0:
           print("Part 2: claim {c}".format(c=row.claim))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day3'), type=str)
    parser.add_argument('--file', default='input.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    overlap = part1(data)

    part2(data, overlap)

