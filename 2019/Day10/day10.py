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

    return np.array(data)


def count_asteroids(x1,y1,asteroids):

    deltas = [(x2 - x1, y2 - y1) for (x2, y2) in asteroids if (x2,y2) != (x1,y1)]
    visible_astroids = set()

    for (dx,dy) in deltas:
        slope = dy/dx
        if (dx < 0) & (dy < 0):
            quad = 1
        elif (dx < 0) & (dy >= 0):
            quad = 2
        elif (dx >= 0) & (dy >= 0):
            quad = 3
        elif (dx >= 0) & (dy < 0):
            quad = 4

        visible_astroids.add((slope,quad))

    num_asteroids = len(set(visible_astroids))

    return num_asteroids


def part1(data):

    width, height = data.shape
    asteroids = np.where(data=='#')
    asteroids = list(zip(asteroids[1],asteroids[0]))

    options = {}

    for (x,y) in asteroids:
        num_asteroids = count_asteroids(x,y,asteroids)
        options[(x,y)] = num_asteroids

    location = max(options,key=options.get)
    print('best location: ', location, " num_visible: ",  options[location])

    return

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day10'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

