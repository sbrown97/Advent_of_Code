from collections import defaultdict
import heapq
import os
import argparse

class TreeNode:
  def __init__(self, name, value):
    self.name = name # node name
    self.value = value # distance from COM
    self.children = [] # references to other nodes
    self.parent = None # references to other nodes

  def get_neighbors(self):
    neighbors = [child.name for child in self.children]
    if self.parent:
        neighbors = neighbors + [self.parent.name]
    return neighbors

  def add_child(self, child_node):
    # creates parent-child relationship
    #print("Adding " + child_node.name)
    self.children.append(child_node) 
    child_node.parent = self
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    #print("Removing " + child_node.name + " from " + self.name)
    self.children = [child for child in self.children 
                     if child is not child_node]
    child_node.parent = [parent for parent in child_node.parent if parent is not self]

  def sum_orbits(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    orbits = 0
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      orbits += current_node.value
      nodes_to_visit += current_node.children

    return orbits


def parse_input(path):
    """ read in and parse input data
    returns tree with children orbiting parents and value = distance from COM"""
    
    data = {}
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(')')
            #data.append(l)

            if l[0] in data:
                data[l[0]].append(l[1])
            else:
                data[l[0]] = [l[1]]

    return data


def part1(data):

    parent = 'COM'
    nodes = {parent:TreeNode(parent,0)}        
    buildTree(nodes,data,parent)
        
    print(nodes['COM'].sum_orbits())

    return nodes

def buildTree(nodes, data, parent):
    
    parent_value = nodes[parent].value
    children = data[parent]
    for kid in children:
        kid_node = TreeNode(kid,parent_value + 1)
        nodes[kid] = kid_node
        nodes[parent].add_child(kid_node)

        if kid in data.keys():
            buildTree(nodes, data, kid)
        
def dijkstras(data,source,sink):
    # dijkstra's algorithm - updated to use priority queue
    
    allnodes = set(data.keys()) # all valid nodes
    prev = {} # previous node in the path to a given node
    nodes = [] # nodes for consideration
    visited = set() # nodes that have been visited
    
    # initialize previous nodes to be None
    for key in data.keys():
        prev[key] = None
    
    # dictionary of distances
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    # first node to consider is the source
    heapq.heappush(nodes, (0, source))

    # while there are still nodes to consider
    while nodes:
        # get node with minimum distance from the source
        _, n = heapq.heappop(nodes)
        visited.add(n)
 
        # stop if the target has been reached 
        if n == sink:
            print(dist[n])
            break

        # candidate neighbors are parents and children
        neighbors = data[n].get_neighbors()
            
        for n2 in neighbors:
            if (n2 in visited) or (n2 not in allnodes):
                # skip this neighbor if it has already been visited or isn't a valid node
                continue
            
            # distance from source if neighbor added to current path
            newDist = dist[n] + 1
            if dist[n2] > newDist:
                # set previous node for this neighbor
                prev[n2] = n
                # update distance from source
                dist[n2] = newDist
                # add  neighbor to nodes for consideration
                heapq.heappush(nodes, (newDist, n2))
        
    return dist, prev

def part2(nodes):

    dijkstras(nodes,nodes['YOU'].parent.name,nodes['SAN'].parent.name)
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day6'), type=str )
    parser.add_argument('--file', default='input.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    nodes = part1(data)

    part2(nodes)

