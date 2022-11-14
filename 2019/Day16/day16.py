import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        l = f.readlines()
        l = l[0].replace('\n','')
        data = [int(x) for x in l]
        
    return data


def phase(signal):

    base_pattern = [0,1,0,-1]
    output = []

    for i in range(len(signal)): # for each value in the signal
        # get the pattern
        pattern = np.repeat(base_pattern,i+1) # repeat each character i+1 times
        pattern = list(pattern) * (int(np.ceil(len(signal) / len(pattern))) + 1) # repeat the whole pattern to exeed the signal length
        pattern = pattern[1:len(signal) + 1] # offset by 1 and match signal length

        # do the sum product
        digit = sum(s*p for s,p in zip(signal, pattern))
        digit = abs(digit) % 10 # only save the ones digit

        # save the new digit
        output.append(digit)

    return output


def part1(data):

    signal = data.copy()

    for i in range(100):
        signal = phase(signal)

    print(signal[:8])
    return

def part2(data):

    signal = data * 10000
    offset = int(''.join([str(x) for x in data[:8]]))

    for i in range(100):
        if i % 10 == 0:
            print(i)

        signal = phase(signal)

    answer = signal[offset:offset+8]    

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day16'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

