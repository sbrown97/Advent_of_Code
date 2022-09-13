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
            l = l.split(',')
            data.append(l)  

    return data

def manhattanDistance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)


def buildWireMap(data):
    
    all_steps = []
    all_points = []
    max_x = 0
    max_y = 0
    for wire in data:
        x, y = 0, 0
        points = set()
        steps = {}
        dist = 0
        for instruction in wire:
            direction = instruction[0]
            length = int(instruction[1:])

            if direction == 'R':
                for i in range(x, x + length, 1):
                    points.add((i + 1, y))
                    dist += 1
                    steps[(i + 1, y)] = dist
                x += length
            elif direction == 'L':
                for i in range(x, x - length, -1):
                    points.add((i - 1, y))
                    dist += 1
                    steps[(i - 1, y)] = dist
                x -= length
            elif direction == 'U':
                for j in range(y, y + length, 1):
                    points.add((x, j + 1))
                    dist += 1
                    steps[(x, j + 1)] = dist
                y += length
            elif direction == 'D':
                for j in range(y, y - length, -1):
                    points.add((x, j - 1))
                    dist += 1
                    steps[(x, j - 1)] = dist
                y -= length
            else:
                print("Invalid direction: ", instruction)

            # update max values
            if abs(x) > max_x:
                max_x = abs(x)
            if abs(y) > max_y:
                max_y = abs(y)
        
        all_points.append(points)
        all_steps.append(steps)

    return all_points, max_x, max_y, all_steps


def part1(data):

    all_points, max_x, max_y, all_steps = buildWireMap(data)

    min_distance = manhattanDistance(0, 0, max_x, max_y)

    for (x,y) in all_points[0].intersection(all_points[1]):
        dist = manhattanDistance(0, 0, x, y)
        if dist < min_distance:
            min_distance = dist

    print(min_distance)
    return all_points, all_steps

def part2(all_points, all_steps):

    min_steps = all_steps[0][max(all_steps[0], key=all_steps[0].get)] + all_steps[1][max(all_steps[1], key=all_steps[1].get)]
    for (x,y) in all_points[0].intersection(all_points[1]):
        steps = all_steps[0][(x,y)] + all_steps[1][(x,y)]
        if steps < min_steps:
            min_steps = steps

    print(min_steps)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day3'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    all_points, all_steps = part1(data)

    part2(all_points, all_steps)

