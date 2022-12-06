import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        data = f.readlines()
        data = data[0]
        data = data.replace('\n','')

    return data


def part1(data):

    for i in range(4,len(data)):
        window = set(data[i-4:i])
        if len(window) == 4:
            print('start of packet: ',i)
            break

    return

def part2(data):

    for i in range(14,len(data)):
        window = set(data[i-14:i])
        if len(window) == 14:
            print('start of packet: ',i)
            break

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day6'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

