
from collections import defaultdict
import os
import argparse
from itertools import permutations
from intcoder import Intcoder

def parse_input(path):
    """ read in and parse input data
    returns """
    

    with open(path) as f:
        l = f.read()
        l = l.replace('\n','')
        l = l.split(',')
        data = defaultdict(int)
        for i in range(len(l)):
            data[i] = int(l[i])
            
    return data

def executeLoop(amps,sequence,input,signal_only=False):

    for i in range(len(sequence)):
        if signal_only:
            amps[i].provide_input(input)
        else:
            amps[i].provide_input([sequence[i], input])
        amps[i].run()
        
        if amps[i].status == -1:
            input = amps[i].get_output()
        
    return input

def part1(data):

    max_output = 0
    amps = [Intcoder(data) for i in range(5)]
    
    for sequence in permutations([0,1,2,3,4]):
        # reset all amps before testing new sequence
        for i in range(5):
            amps[i].reset()

        output = executeLoop(amps,sequence,0)
        if output > max_output:
            max_output = output

    print('Part 1: ',max_output)

    return

def part2(data):

    max_output = 0
    amps = [Intcoder(data) for i in range(5)]

    for sequence in permutations([5,6,7,8,9]):
        # reset all amps be fore testing new sequence
        for i in range(5):
            amps[i].reset()

        output = executeLoop(amps,sequence,0)

        while amps[-1].status != 0:
            output = executeLoop(amps,sequence,output,signal_only=True)

        if output > max_output:
            max_output = output

    print("Part 2: ",max_output)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day7'), type=str, help=f'''''')
    parser.add_argument('--file', default='input.txt',type=str, help=f'''''')
    #TODO: why doesn't test 4 work?
    
    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))
    
    part1(data)

    part2(data)