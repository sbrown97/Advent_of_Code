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
            l = l.replace('\n','').strip()
            # TODO: replace with regex for replacing consecutive spaces with comma
            row = []
            for x in l.split(' '):
                if x != '':
                    row.append(int(x))

            data.append(row)

    return data


def part1(data):
    """ check whether the sum of the two smallest numbers are greater than the largest number in each candidate"""

    triangles = 0

    for candidate in data:
        sorted_data = sorted(candidate)
        if sum(sorted_data[:2]) > sorted_data[2]:
            triangles += 1

    print(f'Part 1: possible triangles {triangles}')


def part2(data):

    triangles = 0
    data = np.array(data)

    for i in range(0,len(data),3):
        col1 = sorted(data[i:i+3,0])
        col2 = sorted(data[i:i+3,1])
        col3 = sorted(data[i:i+3,2])

        if sum(col1[:2]) > col1[2]:
            triangles += 1

        if sum(col2[:2]) > col2[2]:
            triangles += 1
        if sum(col3[:2]) > col3[2]:
            triangles += 1

    print(f'Part 2: {triangles} possible triangles')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2016\\Day3'), type=str)
    parser.add_argument('--file', default='input.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)
