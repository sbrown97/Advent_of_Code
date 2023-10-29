import numpy as np
import pandas as pd
import argparse
from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self,data):
        self.head = Node(data)
        self.head.next = self.head
        self.head.prev = self.head

    def move_right(self,steps):
        for i in range(steps):
            self.head = self.head.next

    def move_left(self,steps):
        for i in range(steps):
            self.head = self.head.prev

    def pop_node(self):
        node = self.head
        new_head = node.next
        prev = node.prev

        self.head = new_head
        prev.next = new_head
        self.prev = prev

        return node.data

    def insert(self, data, index=0):
        new_node = Node(data)
        current_node = self.head
        position = 0

        while (current_node != None) and (position != index):
            position += 1
            current_node = current_node.next

        if current_node != None:
            next_node = current_node.next
            new_node.next = next_node
            new_node.prev = current_node
            current_node.next = new_node
            next_node.prev = new_node
            self.head = new_node

        else: 
            print("Index not present")

    def print_list(self):
        node = self.head
        results = [node.data]
        while node.next != self.head:
            node = node.next
            results.append(node.data)

        print(results)
        

def play(players,max_marble):

    p = 0 # current player index (-1 from their ID)
    marbles = doubly_linked_list(0)
    scores = defaultdict(int)

    for m in range(1,max_marble + 1):
        if m % 23 == 0:
            scores[p + 1] += m
            marbles.move_left(7)
            scores[p + 1] += marbles.pop_node()
            
        else:
            marbles.insert(m,1)

        p += 1
        p %= players

    return scores


def part1(players, max_marble):

    scores = play(players,max_marble)
    print("Part 1: {x}".format(x = scores[max(scores,key=scores.get)]))
    return


def part2(players, max_marble):

    scores = play(players,max_marble*100)
    print("Part 2: {x}".format(x = scores[max(scores,key=scores.get)]))
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--players', default=9, type=int)
    parser.add_argument('--max_marble', default=25,type=int)

    args = parser.parse_args()

    part1(args.players, args.max_marble)

    part2(args.players, args.max_marble)

