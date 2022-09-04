import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        l = f.read()
        l = l.replace('\n','')
        l = l.split(',')
        data = [int(x) for x in l]
        
    return data


def part1(data):
    """ execute Intcode 
            opcode 1 - add values in the positions specified by the next two terms and overwrite value in position specified by 3rd term
            opcode 2 - same but multiply
            opcode 99 - terminate program
        return: value in position 0"""

    # restore gravity assist
    data[1] = 12
    data[2] = 2
    
    for i in range(0,len(data),4):
        #print('data[i:i+4]: ', data[i:i+4])
        opcode = data[i]
        if opcode == 99:
            break
        else:
            idx1 = data[i+1]
            idx2 = data[i+2]
            term1 = data[idx1]
            term2 = data[idx2]
            pos = data[i+3]
            if opcode == 1:
                data[pos] = term1 + term2
            elif opcode == 2:   
                data[pos] = term1 * term2

        #print(' opcode: ', opcode, ' term1: ', term1, ' term2: ', term2,' pos: ', pos, ' value: ',data[pos], data[i:i+4])
        

    return data[0]

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day2'), type=str, help=f'''''')
    parser.add_argument('--file', default='input.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    print('Part1: ', part1(data))

    part2(data)

