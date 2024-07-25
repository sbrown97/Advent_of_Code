from collections import Counter
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = pd.read_csv(path,header=None,names=['x','y'])

    return data


def part1(data):

    # any coord at the min or max x or y value will have an infinite area
    min_x = min(data.x)
    max_x = max(data.x)
    min_y = min(data.y)
    max_y = max(data.y)
    area_counter = Counter()
    inf_coords = set()

    for x in range(min_x,max_x + 1):
        for y in range(min_y,max_y + 1):
            dists = abs(data.x - x) + abs(data.y - y)
            closest = dists.idxmin()
            if len(dists[dists == dists.min()]) == 1:
                area_counter.update([closest])
                if (x in [min_x,max_x]) | (y in [min_y, max_y]) :
                    inf_coords.add(closest)

    counter_subset = {key: area_counter[key] for key in area_counter.keys() if key not in inf_coords}
    max_area = max(counter_subset.values())
    print("Part 1: {x}".format(x=max_area))

    return

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day6'), type=str)
    parser.add_argument('--file', default='input.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

