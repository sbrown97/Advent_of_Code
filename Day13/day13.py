import numpy as np
import os
import argparse
import math

from sqlalchemy import false



def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        data = f.readlines()  

    earliest_departure = int(data[0].replace('\n',''))
    bus_ids = data[1].replace('\n','').split(',')
    buses = [int(b) for b in bus_ids if b != 'x' ]
    offsets = [bus_ids.index(str(x)) for x in buses]

    return earliest_departure, buses, offsets


def part1(earliest_departure, buses):
    """Each bus departs at multiples of it's id number.
    Find the bust that departs soonest after the earliest_departure time"""
    
    next_departure = [math.ceil(time/b) * b for b in buses]

    departure = min(next_departure)
    bus = buses[next_departure.index(departure)]
    wait = departure - time

    print(bus * wait)

    return   


def chinese_remainder_theorem(buses, offsets):

    bi = []
    for i in range(len(buses)):
        r = (buses[i] - (offsets[i]%buses[i])) % buses[i]
        bi.append(r)

    N = 1
    for i in range(len(buses)):
        N *= buses[i]

    Nis = [N // b for b in buses]

    xis = []
    for i in range(len(buses)):
        x = 1
        y = Nis[i] % buses[i]
        found = False
        while not found:
            if (y * x) % buses[i] == 1:
                found = True
                break
            x += 1
        xis.append(x)

    total = 0
    for i in range(len(buses)):
        total += (bi[i] * Nis[i] * xis[i])

    return total % N


def part2(buses, offsets):
    """find the timesep t where each bus departs at it's offset timesteps after t"""

    t = chinese_remainder_theorem(buses,offsets)
    print(t)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day13'), type=str, help=f'''''')
    parser.add_argument('--file', default='input.txt',type=str, help=f'''''')

    args = parser.parse_args()

    time, buses, offsets = parse_input(os.path.join(args.input_dir,args.file))

    part1(time, buses)

    part2(buses, offsets)

