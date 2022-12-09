import math
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = pd.read_csv(path,sep=' ',header=None,names=['direction','steps'])
    return data


def moveHead(direction,h_x,h_y):
    # move H
    if direction == 'U':
        h_y += 1
    elif direction == 'D':
        h_y -= 1
    elif direction == 'L':
        h_x -= 1
    elif direction == 'R':
        h_x += 1
    else:
        print('INVALID DIRECTION')
    return h_x,h_y


def moveTail(h_x,h_y,t_x,t_y):

    # move T
    
    distance = math.sqrt((h_x - t_x)**2 + (h_y - t_y)**2)
    if distance >= 2:
        # move horizontally
        if (h_y == t_y):
            t_x += (h_x - t_x)/abs(h_x - t_x)

        # move vertically
        elif (h_x == t_x):
            t_y += (h_y - t_y)/abs(h_y - t_y)

        # move diagonally
        else:
            t_x += (h_x - t_x)/abs(h_x - t_x)
            t_y += (h_y - t_y)/abs(h_y - t_y)

    return t_x,t_y


def part1(data):

    h_x =0
    h_y = 0
    t_x = 0
    t_y = 0
    t_visit = set()
    t_visit.add((t_x,t_y))

    for instruction in data.itertuples():
        for step in range(instruction.steps):
            
            h_x,h_y = moveHead(instruction.direction,h_x,h_y)
            t_x,t_y = moveTail(h_x,h_y,t_x,t_y)
            t_visit.add((t_x,t_y))

    print(len(t_visit))
    return

def part2(data):
    
    knots_x = [0] * 10
    knots_y = [0] * 10
    t_visit = set()
    t_visit.add((0,0))

    for instruction in data.itertuples():
        for step in range(instruction.steps):
            knots_x[0], knots_y[0] = moveHead(instruction.direction,knots_x[0],knots_y[0])
            for knot in range(9):
                knots_x[knot+1],knots_y[knot+1] = moveTail(knots_x[knot],knots_y[knot],knots_x[knot+1],knots_y[knot+1])

            t_visit.add((knots_x[-1],knots_y[-1]))

    print(len(t_visit))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day9'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

