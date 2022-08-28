import numpy as np
import pandas as pd
import os
import argparse
from collections import Counter

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = pd.DataFrame(columns=['letter','minimum','maximum','password'])
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(': ')
            rule = l[0].split(' ')
            letter = rule[1]
            data = data.append({'letter':letter,'minimum':int(rule[0].split('-')[0]),
                                'maximum':int(rule[0].split('-')[1].split(' ')[0]),
                                'password':l[1]},ignore_index=True)  

    return data


def part1(data):

    num_valid = 0
    for row in data.itertuples():
        letters = Counter(row.password)
        if (letters[row.letter] >= row.minimum) and (letters[row.letter] <= row.maximum):
            num_valid += 1

    print(num_valid)

    return

def part2(data):

    num_valid = 0

    for row in data.itertuples():
        if int(row.password[row.minimum-1] == row.letter) + int(row.password[row.maximum-1] == row.letter) == 1:
            num_valid += 1

    print(num_valid)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day2'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

