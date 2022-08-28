import numpy as np
import pandas as pd
import os
import argparse
from collections import Counter

def parse_input(path):
    """ read in and parse input data
    returns a DataFrame with the group id, person id, and response letters for each person"""
    
    data = pd.DataFrame(columns=['group','person','letters'])
    group = 0
    person = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            if len(l) > 0:
                data = data.append({'group':group,'person':person,'letters':l},ignore_index=True)
                person += 1
            else:
                group += 1
                person = 0

    return data


def part1(data):

    sum = 0
    for g in data.group.unique():
        # get list of responses for each person in the current group
        letters = data[data.group == g].letters.values
        # count letter occurances
        count = Counter(''.join(letters))
        # add number of unique letters to running total
        sum += len(count)

    print(sum)
    return

def part2(data):

    sum = 0
    for g in data.group.unique():
        # get list of responses for each person in the current group
        letters = data[data.group == g].letters.values
        # count letter occurances
        count = Counter(''.join(letters))
        for i in count.values():
            # check if the count of this letter matches the number of people
            if i == len(letters):
                sum += 1

    print(sum)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day6'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

