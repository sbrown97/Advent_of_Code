import numpy as np
import pandas as pd
import os
import argparse
import string

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        data = f.readlines()[0]
        data = data.replace('\n','')
        data = data.split(',')

    return data


def dance(data,programs):
    for dance_move in data:
        if dance_move[0] == 's':
            # spin - move num characters from the end to the beginning of the string
            num = int(dance_move[1:])
            programs = programs[-num:] + programs[:-num]

        elif dance_move[0] == 'x':
            # exchange - swap characters based on position
            A, B = dance_move[1:].split('/')
            A_char = programs[int(A)]
            B_char = programs[int(B)]
            programs[int(A)] = B_char
            programs[int(B)] = A_char

        elif dance_move[0] == 'p':
            # partner - swap characters
            A_char, B_char = dance_move[1:].split('/')
            A = programs.index(A_char)
            B = programs.index(B_char)
            programs[A] = B_char
            programs[B] = A_char

        else:
            print(f'invalid instruction {dance_move}')

    return programs

def part1(data,num_chars):

    programs = list(string.ascii_lowercase[:num_chars])

    programs = dance(data,programs)

    print(f'Part 1: {''.join(programs)}')
    return

def part2(data,num_chars):
    # this is still slow and i don't think it's right because the partnering instructions mean you can't just repeat the same index shuffling

    letters = list(string.ascii_lowercase[:num_chars])
    programs = dance(data,letters)

    dance_map = {}
    for i in range(num_chars):
        dance_map[i] = programs.index(letters[i])

    for i in range(1000000000):
        letters = dance(data,letters)
        if i % 1000000 == 0:
            print(f'round {i}')


    print(f'Part 2: {''.join(letters)}')
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2017\\\Day16'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--num_chars', default=5, type=int)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data,args.num_chars)

    part2(data,args.num_chars)

