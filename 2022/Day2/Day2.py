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

            # map Rock = 1, Paper = 2, Scisors = 3
            l = l.replace('X','1')
            l = l.replace('Y','2')
            l = l.replace('Z','3')
            l = l.replace('A','1')
            l = l.replace('B','2')
            l = l.replace('C','3')

            row = [int(x) for x in l.split(' ')]
            data.append(row)  

    return data


def scoreTurn(opponent_move, my_move):
    
    moves = [1,2,3]

    total_score = my_move

    if my_move == opponent_move: # draw
        total_score += 3
    elif moves[opponent_move - 2] == my_move : # I loose
        total_score += 0
    else: # I win
        total_score += 6
    
    return total_score

def part1(data):

    total_score = 0

    for turn in data:
        opponent_move = turn[0]
        my_move = turn[1]
        total_score += scoreTurn(opponent_move,my_move)
        

    print(total_score)


    return

def part2(data):

    total_score = 0
    moves = [1,2,3]

    for turn in data:
        opponent_move = turn[0]
        outcome = turn[1]

        if outcome == 1: # loose
            my_move = moves[opponent_move - 2]
        elif outcome == 2: # draw
            my_move = moves[opponent_move - 1]
        else: # win
            my_move = moves[opponent_move - 3]

        total_score += scoreTurn(opponent_move,my_move)

    print(total_score)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day2'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

