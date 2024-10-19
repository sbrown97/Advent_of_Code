import numpy as np
import pandas as pd
import os
import argparse
from collections import Counter
from itertools import combinations
import jellyfish

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
    '''
    multiply the number of entries that have a letter that repeates exactly twice by the number
    of entries that have a letter that repeates exactly three times
    '''

    doubles = 0
    triples = 0

    for id in data:
        count = Counter(id)
        if 2 in count.values():
            doubles += 1
        if 3 in count.values():
            triples += 1

    checksum = doubles * triples
    print("Part 1: " + str(checksum))

    return

def part2(data):
    '''
    find the most similar pair of strings and return their common letters
    '''

    id_lengths = len(data[0]) # assumes that all strings are the same length

    min_dist = id_lengths + 1
    
    for (s1,s2) in combinations(data,2):
        dist = jellyfish.damerau_levenshtein_distance(s1,s2)
        if dist < min_dist:
            min_dist = dist
            closest_pair = (s1,s2)

    (s1,s2) = closest_pair
    common = [s1[i] for i in range(id_lengths) if s1[i] == s2[i]]

    print("Part 2: " + ''.join(common))
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\\Day2'), type=str)
    parser.add_argument('--file', default='test2.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

