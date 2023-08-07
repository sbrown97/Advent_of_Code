import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    rules = {}
    with open(path) as f:

        i = 0

        for l in f:
            l = l.replace('\n','')
            
            if i == 0:
                pots = l.replace('initial state: ','')
            elif i > 1:
                l = l.split(' => ') 
                rules[l[0]] = l[1]

            i += 1

    return pots, rules


def applyRules(state,rules,offset):

    new_state = []

    for i in range(-2,len(state)+2):
        # get subset of pots
        if i < 2:
            pattern = '.'*(2 - i) + state[:3 + i]
        elif i < len(state) - 2:
            pattern = state[i-2:i+3]
        else:
            pattern = state[i-2:] + '.'*(3 + i - len(state))

        # apply rule
        if pattern in rules:
            plant = rules[pattern]
        else:
            plant = '.' 

        new_state.append(plant)
        
    # only keep extra left pots if they contain plants
    new_state = ''.join(new_state)
    if new_state[0] == '#':
        offset -= 2
    elif new_state[1] == '#':
        offset -= 1
        new_state = new_state[1:]
    else:
        new_state = new_state[2:]
    
    if new_state[-2:] == '..':
        new_state = new_state[:-2]
    elif new_state[-2:] == '#.':
        new_state = new_state[:-1]

    return new_state, offset

def part1(pots,rules,num_steps):
    '''
    apply the rules to determine which pots have plants after num_steps
    pots: '#' = has a plant, '.' = no plant
    rules: 'LLCRR': N
    if no rule for a given pattern, assume it results in no plant 
    '''

    idx_start = 0
    new_pots = pots

    for s in range(num_steps):
        new_pots, idx_start = applyRules(new_pots,rules,idx_start)
        

    plant_idxs = [idx_start + i for i in range(len(new_pots)) if new_pots[i] == '#']
    print("Part 1: " + str(sum(plant_idxs)))

    return

def part2(pots, rules):
    '''
    same as part 1, but scale up to 5B steps
    '''

    plants = [i for i in range(len(pots)) if pots[i] == '#']

    #for s in range(50000000000):


    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day12'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--num_steps', default=20, type=int)

    args = parser.parse_args()

    pots, rules = parse_input(os.path.join(args.input_dir,args.file))

    part1(pots, rules, args.num_steps)

    part2(pots, rules)

