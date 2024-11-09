import numpy as np
import pandas as pd
import os
import argparse
from collections import Counter

def parse_input(path):
    """ read in and parse input data
    returns """
    
    disks = {}
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            data = l.split(" ")
            name = data[0]
            weight = int(data[1][1:-1])

            # create disk
            if name in disks:
                disks[name].weight = weight
            else:
                node = Disk(name,weight)
                disks[name] = node

            # add any child-parent relationships
            if "->" in l:
                for child in data[3:]:
                    child_name = child.replace(',','')
                    if child_name not in disks:
                        child_node = Disk(child_name)
                        disks[child_name] = child_node

                    disks[name].add_child(disks[child_name])
                    

    return disks


def part1(data):
    # find head of the tree
    disk = data[list(data.keys())[0]]
    while disk.parent:
        disk = disk.parent

    print(f'Part 1: {disk.name}')

    tree = Tower(disk,data)

    return tree

def part2(tree):

    node = tree.head

    # calculate total weights for all nodes in tree
    node.calc_weights()

    node.check_balance()



    return 


class Disk:

    def __init__(self,name,weight=0) -> None:
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def add_child(self,child) -> None:
        self.children.append(child)
        child.parent = self

    def get_tower_weight(self) -> int:
        total_weight = self.weight
        for child in self.children:
            total_weight += child.get_tower_weight()

        self.total_weight = total_weight
        return total_weight

    def calc_weights(self) -> None:

        for child in self.children:
            child.get_tower_weight()
    
    def check_balance(self):
        # get total weight of each child
        child_weights = {c: c.total_weight for c in self.children}

        balance_counter = Counter(child_weights.values())
        if len(balance_counter) > 1:
            mismatch = min(balance_counter,key=balance_counter.get) # total weight of the mismatched node
            bad_node = [k for k, v in child_weights.items() if v == mismatch][0]

            result = bad_node.check_balance()
            if result == True:
                # children of bad node are balanced, so this is where we stop
                desired_weight = max(balance_counter,key=balance_counter.get)
                print(f'Part 2: bad node: {bad_node.name}, needed weight: {desired_weight - mismatch + bad_node.weight}')
        else:
            return True



class Tower:

    def __init__(self, head, nodes) -> None:
        self.head = head
        self.nodes = nodes

    def find_imbalance(self):

        node = self.head
        balanced_nodes = []
        node = self.check(node,balanced_nodes)

    def check(self, node, balanced_nodes):
        
        for child in node.children:
            if child.check_balance():
                balanced_nodes.append(child)
            else:
                self.check(child,balanced_nodes)
                return child


    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day7'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    tree = part1(data)

    part2(tree)

