import numpy as np
from collections import defaultdict
import heapq
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
            row = [ord(x) - 96 for x in l]
            data.append(row)  

    data = np.array(data)

    start = np.where(data == -13)
    start = list(zip(start[0], start[1]))[0]
    data[start] = 1

    end = np.where(data == -27)
    end = list(zip(end[0],end[1]))[0]
    data[end] = 26

    return data, start, end


def dijkstras(data, source, sink):
    # dijkstra's algorithm - updated to use priority queue
    
    allnodes = set() # all valid nodes
    prev = {} # previous node in the path to a given node
    nodes = [] # nodes for consideration
    visited = set() # nodes that have been visited
    
    # build all valid nodes and initialize previous nodes to be None
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            allnodes.add((i,j))
            prev[(i,j)] = None
    
    # dictionary of distances
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    # first node to consider is the source
    heapq.heappush(nodes, (0, source))

    # while there are still nodes to consider
    while nodes:
        # get node with minimum distance from the source
        _, (i,j) = heapq.heappop(nodes)
        visited.add((i,j))
 
        # stop if the target has been reached 
        if (i,j) == sink:
            break

        # candidate neighbors are up/down/right/left
        neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            
        for (r,c) in neighbors:
            if ((r,c) in visited) or ((r,c) not in allnodes):
                # skip this neighbor if it has already been visited or isn't a valid node
                continue
            elif data[(r,c)] - data[(i,j)] > 1:
                # skip this neighbor because the elevation increase is too much
                continue
            
            # distance from source if neighbor added to current path
            newDist = dist[(i,j)] + 1
            if dist[(r,c)] > newDist:
                # set previous node for this neighbor
                prev[(r,c)] = (i,j)
                # update distance from source
                dist[(r,c)] = newDist
                # add  neighbor to nodes for consideration
                heapq.heappush(nodes, (newDist, (r,c)))
        
    return dist, prev

    
def part1(data, start, end):

    dist, prev = dijkstras(data,start,end)
    print(dist[end])

    return 

def part2(data,end):

    result = np.where(data == 1)
    starts = list(zip(result[0],result[1]))
    min_dist = data.size + 1
    for s in starts:
        dist, prev = dijkstras(data,s,end)
        if dist[end] < min_dist:
            min_dist = dist[end]
            min_s = s

    print(min_dist)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day12'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data, start, end = parse_input(os.path.join(args.input_dir,args.file))

    part1(data, start, end)

    part2(data,end)

