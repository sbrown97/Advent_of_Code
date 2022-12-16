import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = {}
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(':')
            sensor = l[0].split(',')
            sensor = (int(sensor[0].split('=')[-1]),int(sensor[1].split('=')[-1]))
            beacon = l[1].split(',')
            beacon = (int(beacon[0].split('=')[-1]),int(beacon[1].split('=')[-1]))

            x_max = max(x_max,sensor[0],beacon[0])
            x_min = min(x_min,sensor[0],beacon[0])
            y_max = max(y_max,sensor[1],beacon[1])
            y_min = min(y_min,sensor[1],beacon[1])

            data[sensor] = beacon

    return data


def part1(data,y):

    # build a dictionary with keys = y indices and values = set(non-beacon x indices)
    non_beacons = set()  
    
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in data.items():
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        if y not in range(sensor_y - distance,sensor_y + distance + 1):
            continue

        y_delta = abs(sensor_y - y)
        for x_delta in range(0, distance - y_delta + 1):
                
                if x_delta + y_delta == 0:
                    continue

                for mult in [-1,1]:
                    x = sensor_x + mult * x_delta
                    
                    if (x,y) != (beacon_x,beacon_y):
                        non_beacons.add(x)
                        
    print(len(non_beacons))
    return

def part2(data,max_coord):

    # build a dictionary with keys = y indices and values = set(non-beacon x indices)
    distances = {}
    
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in data.items():
        distances[(sensor_x,sensor_y)] = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    i = 0
    for sensor, dist in distances.items():
        i += 1
        print('Checking sensor {i} of {x}'.format(i=i,x=len(data)))
        # check perimiter points
        for x_delta in range(0,dist + 2):
            y_delta = dist - x_delta + 1

            for x_mult, y_mult in [(1,1),(1,-1),(-1,-1),(-1,1)]:
                x = sensor[0] + x_mult * x_delta
                y = sensor[1] + y_mult * y_delta

                if (x < 0) or (x > max_coord) or (y < 0) or (y > max_coord):
                    continue

                if (x,y) in data: # sensor
                    continue
                elif (x,y) in data.values(): # beacon
                    continue
                
                flag = True
                for sensor_2, dist_2 in distances.items():
                    if abs(sensor_2[0] - x) + abs(sensor_2[1] - y) <= dist_2: # within range of a sensor
                        flag = False
                        break

                if flag:
                    # if we've made it this far we must be the distress signal
                    print(x * 4000000 + y)
                    break
            
            if flag:
                break
        
        if flag:
            break

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day15'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--row',default=10,type=int)
    parser.add_argument('--max_coord',default=20,type=int)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data,args.row)

    part2(data,args.max_coord)

