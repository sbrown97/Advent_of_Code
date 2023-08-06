import numpy as np
import pandas as pd
import os
import argparse

class Instruction:
    def __init__(self,name):
        self.name = name # instruction step name
        self.prereqs = [] # references to other instructions
        self.postreqs = [] # references to other instructions

    def add_prereqs(self,step):
        self.prereqs.append(step)
        step.postreqs.append(self)

    def complete_prereq(self,step):
        self.prereqs = [instruction for instruction in self.prereqs
                        if instruction is not step]

    def ready(self):
        return len(self.prereqs) == 0


def parse_input(path):
    """ read in and parse input data
    returns list of instructions
    """
    
    steps = {}

    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(' must be finished before step ')
            s1 = l[0].split(' ')[-1]
            s2 = l[1].split(' ')[0]

            # create steps
            if s1 not in steps: 
                steps[s1] = Instruction(s1)
            if s2 not in steps:
                steps[s2]= Instruction(s2)

            # add prerequisite relationship
            steps[s2].add_prereqs(steps[s1])

    # sort steps alphabetically
    myKeys = list(steps.keys())
    myKeys.sort()
    steps = {i: steps[i] for i in myKeys}

    return steps

def part1(data):
    '''
    determine the order in which to perform instructions 
    choose alphabetically in the case of a tie    
    '''

    order = []
    keys = list(data.keys())
    keys.sort()

    while len(keys) > 0:
        for name in keys:
            if data[name].ready():
                order.append(name)
                # update prerequisites
                for postreq in data[name].postreqs:
                    postreq.complete_prereq(data[name])
                
                keys.remove(name)
                break

    print('Part 1: ' + ''.join(order))
    return

class Worker:
    def __init__(self,name):
        self.name = name
        self.task = None # name of the current task
        self.time_remianing = 0 # time remaining until finish current task
    
    def startTask(self,task,duration):
        self.task = task
        self.time_remianing = duration

    def busy(self):
        return self.time_remianing > 0

def part2(steps,num_workers,duration):
    '''
    how long does it take to complete all instructions with num_workers working in parallel
    and each instruction takes duration + alphabetical order
    '''

    time = -1
    order = []
    workers = [Worker(i) for i in range(num_workers)]

    keys = list(steps.keys())
    keys.sort()

    while len(keys) > 0:
        time += 1

        # update task progress
        for w in workers:
            if w.busy():
                w.time_remianing -= 1
                # update completed tasks
                if w.time_remianing == 0:
                    # update prerequisites
                    for postreq in w.task.postreqs:
                        postreq.complete_prereq(w.task)          

        # look to start new tasks
        for w in workers:
            if not w.busy():
                for name in keys:
                    if steps[name].ready():
                        order.append(name)
                        d = duration + ord(name.lower()) - 96
                        w.startTask(steps[name],d)
                        
                        keys.remove(name)
                        break


    # finish working final tasks
    while sum([w.busy() for w in workers]) > 0:
        time += 1

        # update task progress
        for w in workers:
            if w.busy():
                w.time_remianing -= 1
                # update completed tasks
                if w.time_remianing == 0:
                    # update prerequisites
                    for postreq in w.task.postreqs:
                        postreq.complete_prereq(w.task)          

    print("Part 1: " + str(time))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day7'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)
    parser.add_argument('--num_workers',default=2,type=int)
    parser.add_argument('--duration',default=0,type=int)

    args = parser.parse_args()

    steps = parse_input(os.path.join(args.input_dir,args.file))

    data = steps.copy()
    part1(data)

    steps = parse_input(os.path.join(args.input_dir,args.file))
    part2(steps,args.num_workers,args.duration)

