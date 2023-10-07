import numpy as np
import pandas as pd
import os
import argparse
import math
from itertools import product

def computePower(x,y,serial_number):
    """
    compute the power level of a fuel cell using the following rules:
     The power level in a given fuel cell can be found through the following process:
        - Find the fuel cell's rack ID, which is its X coordinate plus 10.
        - Begin with a power level of the rack ID times the Y coordinate.
        - Increase the power level by the value of the grid serial number (your puzzle input).
        - Set the power level to itself multiplied by the rack ID.
        - Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
        - Subtract 5 from the power level. 
    """
    
    rackID = x + 10
    power_level = rackID * y
    power_level += serial_number
    power_level *= rackID
    power_level = math.floor(power_level/100) % 10
    power_level -= 5

    return power_level


def buildPowerMatrix(serial_number):
    power = np.zeros([300,300],dtype=int)

    for x in range(0,300):
        for y in range(0,300):
            power[y][x] = computePower(x,y,serial_number)

    return power


def findMaxPower(power, square_size): 

    x_min = 1
    x_max = 300
    y_min = 1
    y_max = 300

    max_power = -1 * np.inf
    best_x = 0
    best_y = 0

    # interate over 3x3 slices fully contained in the grid
    # x,y is the top left  point of the slice
    for x in range(x_min,x_max - square_size - 1):
        for y in range(y_min, y_max - square_size - 1):

            total_power = power[y:y+square_size,x:x+square_size].sum()

            if total_power > max_power:
                max_power = total_power
                best_x = x
                best_y = y
            
    return best_x, best_y, max_power


def part1(power):

    best_x, best_y, max_power = findMaxPower(power,3)
    print("Part 1: ({x},{y})".format(x=best_x,y=best_y))
    
    return


def part2(power):

    best_x = 0
    best_y = 0
    best_size = 0
    max_power = -1 * np.inf
    

    for size in range(1,3001):
        x,y,current_power = findMaxPower(power,size)
        if current_power > max_power:
            max_power = current_power
            best_size = size
            best_x = x
            best_y = y

    print("Part 2: ({x},{y},{s})".format(x=best_x,y=best_y,s=best_size))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--serial_number', default=8444,type=int)

    args = parser.parse_args()

    power = buildPowerMatrix(args.serial_number)
    part1(power)

    part2(power)

