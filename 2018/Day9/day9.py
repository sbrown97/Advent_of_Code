import numpy as np
import pandas as pd
import argparse
from collections import defaultdict

def part1(players, max_marble):

    p = 0 # current player index (-1 from their ID)
    marbles = [0]
    current_idx = 0
    scores = defaultdict(int)

    for m in range(1,max_marble + 1):
        if m % 23 == 0:
            scores[p + 1] += m
            new_idx = (current_idx - 7) % len(marbles)
            scores[p + 1] += marbles.pop(new_idx)
            current_idx = new_idx
        else:
            new_idx = ((current_idx + 1) % len(marbles)) + 1
            marbles.insert(new_idx,m)
            current_idx = new_idx


        p += 1
        p %= players

    print("Part 1: {x}".format(x = scores[max(scores,key=scores.get)]))
    return

def part2(players, max_marble):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--players', default=9, type=int)
    parser.add_argument('--max_marble', default=25,type=int)

    args = parser.parse_args()

    part1(args.players, args.max_marble)

    part2(args.players, args.max_marble)

