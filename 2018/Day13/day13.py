import numpy as np
import re
import os
import argparse
from collections import Counter

class Cart:
    def __init__(self,id,x,y,facing):
        self.id = id # cart's unique ID
        
        self.x = x # initial x coordinate
        self.y = y # initial y coordinate

        # coordinate that the cart is facing (0 = right, 1 = up, 2 = left, 3 = down)
        self.facing = facing 

        # turning directions that will be cycled through each time the cart reaches an intersection
        self.turn_directions = ['left','straight','right'] 


    def getCoord(self):
        return(self.y,self.x)
    

    def setPosition(self,x,y):
        self.x = x
        self.y = y


    def turn(self,direction):
        
        # update facing value
        if direction == 'left':
            self.facing += 1
        elif direction == 'right':
            self.facing -= 1

        self.facing %= 4


    def move(self):

        if self.facing == 0: # move right
            self.x += 1
        elif self.facing == 1: # move up
            self.y -= 1
        elif self.facing == 2: # move left
            self.x -= 1
        elif self.facing == 3: # move down
            self.y += 1

    def step(self,map):
        
        # move in the direction you are facing
        self.move()

        # get current track from map
        track = map[self.y][self.x]

        # turn, if necessary
        if track == "+": # intersection
            # cycle through turning directions
            direction = self.turn_directions.pop(0)
            self.turn_directions.append(direction)
            self.turn(direction)

        elif track == "\\": # 
            if self.facing in [0,2]:
                self.turn('right')
            elif self.facing in [1,3]:
                self.turn('left')
        
        elif track == "/":
            if self.facing in [1,3]:
                self.turn('right')
            elif self.facing in [0,2]:
                self.turn('left')

            
def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    carts = []
    cart_id = 0
    y = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row = [x for x in l]

            # TODO: make sure it works if multiple carts in a row
            if l.find('>') >= 0: # right facing cart
                matches = [x.span()[0] for x in re.finditer('>',l)]
                for x in matches:
                    carts.append(Cart(cart_id,x,y,0))
                    cart_id += 1
                    row[x] = '-'
            
            if l.find('^') >= 0: # up facing cart
                matches = [x.span()[0] for x in re.finditer('\^',l)]
                for x in matches:
                    carts.append(Cart(cart_id,x,y,1))
                    cart_id += 1
                    row[x] = '|'
            
            if l.find('<') >= 0: # left facing cart
                matches = [x.span()[0] for x in re.finditer('<',l)]
                for x in matches:
                    carts.append(Cart(cart_id,x,y,2))
                    cart_id += 1
                    row[x] = '-'
                
            if l.find('v') >= 0: # down facing cart
                matches = [x.span()[0] for x in re.finditer('v',l)]
                for x in matches:
                    carts.append(Cart(cart_id,x,y,3))
                    cart_id += 1
                    row[x] = '|'

            data.append(''.join(row))  

            y += 1

    map = np.array(data)

    return map, carts


def part1(map,carts):

    tick = 0

    collision = False
    
    while not collision:
        tick += 1
        
        # sort carts by coordinates
        cart_coords = {cart.getCoord(): cart.id for cart in carts}
        sorted_coords = sorted(cart_coords)

        for coords in sorted_coords:
            carts[cart_coords[coords]].step(map)

            # check for collision    
            coord_count = Counter([cart.getCoord() for cart in carts])
            if coord_count.most_common(1)[0][1] > 1:
                collision = True
                break



    print("Part1: {c}".format(c=coord_count.most_common(1)[0]))

    return

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day13'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data, carts = parse_input(os.path.join(args.input_dir,args.file))

    part1(data, carts)

    part2(data)

