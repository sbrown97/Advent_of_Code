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
            data = l.split(' ')

    return data

def decode(data,shift):
    
    message = []
    for word in data:
        x = ''
        for i in word:
            if i.isalpha():
                x += chr(((ord(i.lower()) - 97 - shift) % 26) + 97)
            else:
                x += i
        message.append(x)

    return message

def part1(data):
    shift = 10
    message = decode(data,shift)
    index = [i for i, x in enumerate(message) if x == 'triceratops']
            
    print(f'part 1: {message[index[0]:index[-1]]}')
    return

def part2(data):

    for shift in range(1,26):
        print(f'shift: {shift}')
        message = decode(data,shift)
        if 'triceratops' in message:
            index = [i for i, x in enumerate(message) if x == 'triceratops']
            print(f'part 2: {message[index[0]:index[-1]+1]}')
            break

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'week1'), type=str)
    parser.add_argument('--file1', default='input.txt',type=str)
    parser.add_argument('--file2', default='input_2.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file1))

    part1(data)
    
    data = parse_input(os.path.join(args.input_dir,args.file2))

    part2(data)

