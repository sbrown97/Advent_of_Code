import os
import argparse
from re import X
import pandas as pd

def parse_input(path):
    """read and parse input data
    returns dataframe with columns for instruction and value"""

    data = pd.DataFrame(columns=['instruction','value'])

    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            inst = l[0]
            value = int(l[1:])
            data = data.append({'instruction':inst,'value':value},ignore_index=True)

    return data
    

def move(facing,x,y,instruction,value):

    # clockwise order of cardinal directions
    order = ['N','E','S','W']

    if instruction == 'N': # move north 
        y += value
    elif instruction == 'E': # move east
        x += value
    elif instruction == 'S': # move south
        y -= value
    elif instruction == 'W': # move west
        x -= value
    elif instruction == 'L': # turn left
        facing = order[(order.index(facing) - int(value/90)) % len(order)]
    elif instruction == 'R': # turn right
        facing = order[(order.index(facing) + int(value/90)) % len(order)]
    elif instruction == 'F': # move in the direction you are facing
        if facing == 'N':
            y += value
        elif facing == 'E':
            x += value
        elif facing == 'S':
            y -= value
        elif facing == 'W':
            x -= value

    return facing, x, y


def part1(data):

    # start facing east at origin
    facing = 'E'
    x = 0
    y = 0
    
    # move according to the instructions
    for row in data.itertuples():
        facing, x, y = move(facing,x,y,row.instruction,row.value)

    # sum absolute distances
    manhattan_distance = abs(x) + abs(y)
    print(manhattan_distance)
    return

def move2(x_ship,y_ship,x_waypoint,y_waypoint,instruction,value):

    if instruction == 'N': # move waypoint north
        y_waypoint += value
    elif instruction == 'E': # move waypoint east
        x_waypoint += value
    elif instruction == 'S': # move waypoint south
        y_waypoint -= value
    elif instruction == 'W': # move waypoint west
        x_waypoint -= value
    elif instruction == 'F': # move ship to waypoint
        x_ship += value * x_waypoint
        y_ship += value * y_waypoint
    else: # rotate the waypoint around the ship
        mult = 1 if instruction == 'R' else -1
        num_turns = int(value/90)
        if num_turns == 1:
            x = mult * y_waypoint
            y_waypoint = -1 * mult * x_waypoint
            x_waypoint = x
        elif num_turns == 2:
            x_waypoint = -1 * x_waypoint
            y_waypoint = -1 * y_waypoint
        elif num_turns == 3:
            x = -1 * mult * y_waypoint
            y_waypoint = mult * x_waypoint
            x_waypoint = x    

    return x_ship,y_ship,x_waypoint,y_waypoint


def part2(data):

    # start with ship at origin and waypoint at (10,1)
    x_ship = 0
    y_ship = 0
    x_waypoint = 10
    y_waypoint = 1
    
    for row in data.itertuples():
        x_ship, y_ship, x_waypoint, y_waypoint = move2(x_ship,y_ship,x_waypoint,y_waypoint,row.instruction,row.value)

    manhattan_distance = abs(x_ship) + abs(y_ship)
    print(manhattan_distance)
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day12'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    program = parse_input(os.path.join(args.input_dir,args.file))

    part1(program)

    part2(program)

    