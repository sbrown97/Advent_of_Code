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
            row = [x for x in l]
            data.append(row)  

    return data

def partition(letter,min,max):

    if letter in ['F','L']:
        max = int(min + np.floor((max-min)/2))
    else:
        min = int(min + np.ceil((max-min)/2))

    return min, max


def get_seat(ticket):

    min_row = 0
    max_row = 127
    min_column = 0
    max_column = 7

    for letter in ticket:
        if letter in ['F','B']:
            min_row, max_row = partition(letter,min_row,max_row)
        else:
            min_column, max_column = partition(letter,min_column,max_column)

    return min_row, min_column


def part1(data):

    seat_ids = []

    for ticket in data:
        row, column = get_seat(ticket)
        seat_ids.append((row * 8) + column)

    print(max(seat_ids))  

    return seat_ids

def part2(seat_ids):

    options = set(range(min(seat_ids),max(seat_ids) + 1))
    my_seat = options.difference(seat_ids)

    print(my_seat)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day5'), type=str, help=f'''''')
    parser.add_argument('--file', default='test1.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    seat_ids = part1(data)

    part2(seat_ids)

