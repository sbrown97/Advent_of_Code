import numpy as np
import pandas as pd
import os
import argparse
from copy import deepcopy

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    x_max = 0
    y_max = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row =  [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in l.split(' -> ')]
            for (x,y) in row:
                x_max = x if x > x_max else x_max
                y_max = y if y > y_max else y_max
            data.append(row)  

    data = draw_map(data,x_max,y_max)
    return data


def draw_map(data, x_max, y_max):
    
    map = np.full((y_max + 1,x_max + 1),'.')

    for rock in data:
        for i in range(len(rock) - 1):
            x_1, y_1 = rock[i]
            x_2, y_2 = rock[i+1]
            
            x_start = min(x_1,x_2)
            x_end = max(x_1,x_2)
            y_start = min(y_1,y_2)
            y_end = max(y_1,y_2)

            map[y_start:y_end + 1, x_start:x_end + 1] = '#'

    map[0,500] = '+'


    return map


def move_sand(map, sand_x, sand_y):

    if (sand_y+1 >= map.shape[0]) | (sand_x+1 >= map.shape[1]): #fall into the void
        return (sand_x, sand_y)
    elif map[sand_y+1,sand_x] == '.': # move down
        return move_sand(map,sand_x,sand_y+1)
    elif map[sand_y+1,sand_x-1] == '.': # move down-left
        return move_sand(map,sand_x-1,sand_y+1)
    elif map[sand_y+1,sand_x+1] == '.': # move down-right
        return move_sand(map,sand_x+1, sand_y+1)
    else: #come to rest
        return (sand_x,sand_y)

def part1(data):

    map = deepcopy(data)

    step = 0
    void = False

    while not void:
        step += 1
        sand_x, sand_y = move_sand(map,500,0)
        if (sand_y+1 >= map.shape[0]) | (sand_x+1 >= map.shape[1]):
            void = True
        else:
            map[sand_y,sand_x] = 'o'

    print(step - 1)
    return

def part2(data):

    map = deepcopy(data)
    # add buffer to right side
    map = np.append(map,np.full((map.shape[0],map.shape[0]+1),'.'),axis=1)
    # add floor
    map = np.insert(map,map.shape[0],np.full((1,map.shape[1]),'.'),axis=0)
    map = np.insert(map,map.shape[0],np.full((1,map.shape[1]),'#'),axis=0)
    
    step = 0
    full = False

    while not full:
        step += 1
        sand_x, sand_y = move_sand(map,500,0)
        if(sand_y == 0) & (sand_x == 500):
            full = True
        else:map[sand_y,sand_x] = 'o'

    print(step)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\\Day14'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

