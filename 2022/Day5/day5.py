import numpy as np
import pandas as pd
import os
import argparse
import copy

def parse_input(path):
    """ read in and parse input data
    returns """
    
    stacks = []
    instructions = pd.DataFrame(columns=['stack1','stack2','numCrates'])
    with open(path) as f:
        row = 0
        part = 1
        for l in f:
            row += 1
            l = l.replace('\n','')
            if l == '':
                part = 2
                stacks = {x.pop():x[-2::-1] for x in stacks}
                continue

            if part == 1:
                l = l[1::4]
                
                if row == 1: # initialize stack lists
                    for i in range(len(l)):
                        stacks.append([])

                for i in range(len(l)):
                    if l[i] != ' ':
                        stacks[i].append(l[i])

            else:
                l = l.split(' ')
                instructions = instructions.append({'stack1':l[3], 'stack2':l[5], 'numCrates':int(l[1])},ignore_index=True)

    return stacks, instructions


def part1(stacks, instructions):

    for row in instructions.itertuples():
        for i in range(row.numCrates):
            crate = stacks[row.stack1].pop()
            stacks[row.stack2].append(crate)

    tops = [stacks[x][-1] for x in sorted(stacks.keys())]
    print(''.join(tops))
    return

def part2(stacks, instructions):

    for row in instructions.itertuples():
        crates = []
        for i in range(row.numCrates):
            crates.append(stacks[row.stack1].pop())
        
        stacks[row.stack2] += crates[::-1]

    tops = [stacks[x][-1] for x in sorted(stacks.keys())]
    print(''.join(tops))
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\\Day5'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    stacks, instructions = parse_input(os.path.join(args.input_dir,args.file))

    part1(copy.deepcopy(stacks),instructions)

    part2(stacks,instructions)

