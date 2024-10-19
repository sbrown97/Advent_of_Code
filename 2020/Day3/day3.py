import numpy as np
import os
import argparse
from functools import reduce

def parse_input(path):
    """ read in and parse input data
    returns list of lists"""
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row = [x for x in l]
            data.append(row)  

    return data


def check_for_trees(data,x_change,y_change):
    """ move from the top left corner down and to the right acording to the slope 
    defined by x_change, y_change.  Count the number of trees (i.e. "#") encountered"""

    # initial position in the matrix
    x = 0
    y = 0

    # counter for the number of trees encountered
    num_trees = 0

    # move until you move past the bottom of the matrix
    while y < len(data):
        # check for trees
        if data[y][x] == '#':
            num_trees += 1
            
        # move acording to the slope
        x += x_change
        y += y_change

        # wrap back around if reached the right edge
        x = x % len(data[0])

    return num_trees

def part1(data):

    return check_for_trees(data,3,1)

def part2(data):
    # check the following slopes
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    trees = [check_for_trees(data,x_slope,y_slope) for (x_slope,y_slope) in slopes]
    
    # multiply the number of trees for each slope
    answer = reduce((lambda x, y: x * y),trees)
    return answer


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day3'), type=str )
    parser.add_argument('--file', default='input.txt',type=str )

    args = parser.parse_args()

    tree_map = parse_input(os.path.join(args.input_dir,args.file))

    print(part1(tree_map))

    print(part2(tree_map))

