import numpy as np
import re
import os
import argparse
from collections import Counter
import copy

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
    carts = {}
    cart_id = 0
    y = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row = [x for x in l]

            if l.find('>') >= 0: # right facing cart
                matches = [x.span()[0] for x in re.finditer('>',l)]
                for x in matches:
                    carts[cart_id] = Cart(cart_id,x,y,0)
                    cart_id += 1
                    row[x] = '-'
            
            if l.find('^') >= 0: # up facing cart
                matches = [x.span()[0] for x in re.finditer('\^',l)]
                for x in matches:
                    carts[cart_id] = Cart(cart_id,x,y,1)
                    cart_id += 1
                    row[x] = '|'
            
            if l.find('<') >= 0: # left facing cart
                matches = [x.span()[0] for x in re.finditer('<',l)]
                for x in matches:
                    carts[cart_id] = Cart(cart_id,x,y,2)
                    cart_id += 1
                    row[x] = '-'
                
            if l.find('v') >= 0: # down facing cart
                matches = [x.span()[0] for x in re.finditer('v',l)]
                for x in matches:
                    carts[cart_id] = Cart(cart_id,x,y,3)
                    cart_id += 1
                    row[x] = '|'

            data.append(''.join(row))  

            y += 1

    map = np.array(data)

    return map, carts


def run(map,carts):
    """
    Run simulation until a collision. 
    there must be at least 2 carts in order to avoid an infinite loop
    return: updated carts OR -1 if only 1 cart left
    """
    
    # check that there are enough carts to avoid an infinite loop
    if len(carts) < 2:
        return -1
    
    tick = 0

    collision = False
    
    while not collision:
        tick += 1
        collision_coords = []
        
        # sort carts by coordinates
        cart_coords = {cart.getCoord(): cart_id for cart_id, cart in carts.items()}
        sorted_coords = sorted(cart_coords)

        for coords in sorted_coords:
            
            # skip this cart if already in a collision
            if coords in collision_coords:
                continue

            carts[cart_coords[coords]].step(map)

            # check for collision    
            coord_count = Counter([cart.getCoord() for _, cart in carts.items()])
            if coord_count.most_common(1)[0][1] > 1:
                collision = True
                collision_coords.append(coord_count.most_common(1)[0][0])

    return carts


def part1(map,carts):

    # make a copy of the carts so we don't override the original starting points
    carts_p1 = copy.deepcopy(carts)
    # run simulation until there is a collision
    carts_p1 = run(map,carts_p1)
    
    # find the collision coordinate
    coord_count = Counter([cart.getCoord() for __, cart in carts_p1.items()])
    (y,x) = coord_count.most_common(1)[0][0]

    print("Part1: {c}".format(c=(x,y)))

    return

def part2(map, carts):

    carts_p2 = copy.deepcopy(carts)
    while len(carts_p2) > 1:
        carts_p2 = run(map,carts_p2)

        # find all collisions
        coord_count = Counter([cart.getCoord() for __, cart in carts_p2.items()])
        collisions = [coord for coord in coord_count if coord_count[coord] > 1]

        new_carts = {}
        for cart_id, cart in carts_p2.items():
            coord = (cart.y, cart.x)
            if coord not in collisions:
                new_carts[cart_id] = cart

        carts_p2 = new_carts

    try:
        [(y,x)] = [cart.getCoord() for __, cart in carts_p2.items()]
        print("Part2: {c}".format(c=(x,y)))
    except:
        print("Part2: No carts remain!")
    return 


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\\Day13'), type=str)
    parser.add_argument('--file', default='test2.txt',type=str)

    args = parser.parse_args()

    data, carts = parse_input(os.path.join(args.input_dir,args.file))

    part1(data, carts)

    part2(data, carts)

