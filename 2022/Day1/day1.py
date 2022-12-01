import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    items = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            if l == '':
                data.append(items)
                items = []
            else:
                items.append(int(l))

    data.append(items)

    return data


def part1(data):

    maxCalories = 0

    for elf in data:
        calories = sum(elf)
        if calories > maxCalories:
            maxCalories = calories

    print(maxCalories)

    return

def part2(data):

    totalCalories = [sum(elf) for elf in data]

    totalCalories.sort(reverse=True)
    
    print(sum(totalCalories[:3]))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day1'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

