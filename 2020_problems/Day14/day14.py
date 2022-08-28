import numpy as np
import pandas as pd
import os
import argparse

import itertools

def parse_input(path):
    """ read in and parse input data
    returns """
    
    program = pd.DataFrame(columns=['location','value'])
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(' = ')
            if l[0] == 'mask':
                loc = 'mask'
                value = l[1]
            else:
                loc = int(l[0].replace('mem[','').replace(']',''))
                value = int(l[1])
            program = program.append({'location':loc,'value':value},ignore_index=True)  

    return program


def compute_sum(memory):

    sum = 0
    for (key, value) in memory.items():
        sum += int(value,2)

    return sum


def part1(program):
    
    mask = {}
    memory = {}

    for row in program.itertuples():
        if row.location == 'mask':
            # update mask
            mask = {i:row.value[i] for i in range(len(row.value)) if row.value[i] != 'X'}
        else:
            # convert value to binary
            binary = list(format(row.value,"036b"))
            
            # apply current mask
            for (key,value) in mask.items():
                binary[key] = value
            
            # store in memory
            memory[row.location] = ''.join(binary)

    sum = compute_sum(memory)

    print(sum)

    return

def part2(program):

    bits = ['1','0']
    mask = ''
    memory = {}

    for row in program.itertuples():
        if row.location == 'mask':
            # update mask
            mask = row.value
        else:
            # convert location to binary
            binary = list(format(row.location,"036b"))
            
            # apply current mask
            address = [mask[i] if mask[i] != '0' else binary[i] for i in range(len(mask))]
            
            # generate all memory locations
            for combo in itertools.product(bits,repeat=address.count('X')):
                copy = address.copy()
                for i in combo:
                    copy[copy.index('X')] = i
                
                # store in memeory
                memory[''.join(copy)] = row.value

    print(sum(memory.values()))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day14'), type=str, help=f'''''')
    parser.add_argument('--file', default='test2.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

