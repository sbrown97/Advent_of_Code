import time
import numpy as np
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    positions = []
    velocities = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.replace('<','')
            l = l.replace('>','')
            l = l.split(',')
            coords = [int(x.split('=')[1]) for x in l]
            positions.append(coords) 
            velocities.append([0,0,0]) 

    return np.array(positions), np.array(velocities)


def update_universe(positions, velocities):
    # update velocities
    for moon1 in range(len(positions)):
        # compare this moon's position to all other moons
        for moon2 in range(len(positions)):
            if moon2 != moon1:
                for i in range(3): # assumes 3-dimensional position
                    if positions[moon2][i] > positions[moon1][i]:
                        velocities[moon1][i] += 1
                    elif positions[moon2][i] < positions[moon1][i]:
                        velocities[moon1][i] -= 1

    # update positions
    positions += velocities

    return positions, velocities


def part1(positions, velocities, numSteps):

    # for each step
    for step in range(numSteps): 

        positions, velocities = update_universe(positions,velocities)

    # calculate total energy of the system
    potential_energy = abs(positions).sum(axis=1)
    kinetic_energy = abs(velocities).sum(axis=1)
    energy = potential_energy * kinetic_energy

    print('part1: ', sum(energy))

    return 

def part2(positions, velocities):

    init_pos = positions.copy()
    init_vel = velocities.copy()
    size = 2 * positions.size

    step = 1
    positions, velocities = update_universe(positions,velocities)
    start = time.time()
    while size != ((positions == init_pos).sum() + (velocities == init_vel).sum()):
        
        step += 1
        if step % 100000 == 0:
            print('step: {s}, time: {t}'.format(s=step, t = time.time() - start))

        positions, velocities = update_universe(positions,velocities)

    print(step)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day12'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--steps', default=10, type=int)

    args = parser.parse_args()

    init_positions, init_velocities = parse_input(os.path.join(args.input_dir,args.file))

    part1(init_positions.copy(), init_velocities.copy(), args.steps)

    part2(init_positions.copy(), init_velocities.copy())

