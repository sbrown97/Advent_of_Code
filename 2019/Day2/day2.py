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
    code = data.copy()
    code[1] = 12
    code[2] = 2
    
    return intcode(code)

def intcode(data):

    code = data.copy()
    
    for i in range(0,len(code),4):
        opcode = code[i]
        if opcode == 99:
            break
        else:
            idx1 = code[i+1]
            idx2 = code[i+2]
            term1 = code[idx1]
            term2 = code[idx2]
            pos = code[i+3]
            if opcode == 1:
                code[pos] = term1 + term2
            elif opcode == 2:   
                code[pos] = term1 * term2

    return code[0]


def part2(data):

    for noun in range(100):
        for verb in range(100):
            code = data.copy()

            code[1] = noun
            code[2] = verb
        
            output = intcode(code)

            if output == 19690720:
                answer = 100 * noun + verb
                print(answer)
                return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day2'), type=str, help=f'''''')
    parser.add_argument('--file', default='input.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    print('Part1: ', part1(data))

    part2(data)

