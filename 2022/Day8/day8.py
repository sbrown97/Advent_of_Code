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
            row = [int(x) for x in l]
            data.append(row)  

    return np.array(data)


def part1(data):

    numCol, numRow = data.shape
    visible = 2 * (numCol + numRow) - 4

    for i in range(1,numRow - 1):
        for j in range(1,numCol - 1):
            tree = data[i,j]

            if all(tree > data[:i,j]): # visible from top
                visible += 1
                continue
            elif all(tree > data[i,:j]): # visible from left
                visible += 1
                continue
            elif all(tree > data[i,j+1:]): # visible from right
                visible += 1
                continue
            elif all(tree > data[i+1:,j]): # visible from bottom
                visible += 1
                continue

    print(visible)

    return

def countTrees(view):
    num_trees = 0
    for x in view:
        num_trees += 1
        if not x:
            break
    return num_trees

def part2(data):

    maxScore = 0
    numCol, numRow = data.shape

    for i in range(numRow):
        for j in range(numCol):
            score = 1
            tree = data[i,j]

            # look up
            view = data[:i,j] < tree
            score *= countTrees(view[::-1])


            # look right
            view = data[i,j+1:] < tree
            score *= countTrees(view)

            # look down
            view = data[i+1:,j] < tree
            score *= countTrees(view)

            # look left
            view = data[i,:j] < tree
            score *= countTrees(view[::-1])

            maxScore = score if score > maxScore else maxScore

    print(maxScore)
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day8'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

