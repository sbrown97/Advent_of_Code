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
            data.append(l)  

    return data


def part1(data):
    errors = []
    for rucksack in data:
        numItems = int(len(rucksack)/2)
        compartment1 = set(rucksack[:numItems])
        compartment2 = set(rucksack[numItems:])
        errors.append(list(compartment1.intersection(compartment2)))

    errors = [''.join(x) for x in errors]
    priorities = [ord(x.swapcase()) - 64 if x.islower() else ord(x.swapcase()) - 70 for x in errors]

    print(sum(priorities))

    return

def part2(data):

    badges = []

    for group in range(0,len(data),3):
        rucksacks = data[group:group+3]
        commonItems = set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2]))
        badges.append(list(commonItems))

    badges = [''.join(x) for x in badges]
    priorities = [ord(x.swapcase()) - 64 if x.islower() else ord(x.swapcase()) - 70 for x in badges]

    print(sum(priorities))


    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day3'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

