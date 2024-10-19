import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path, width, height):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            row = [int(x) for x in l]
            
            data += row  

    data = np.array(data)
    num_layers = len(data) / (height * width)
    data = data.reshape(int(num_layers), height, width)

    return data


def part1(data):

    num_layers, _, _ = data.shape
    min_zeros = 9999
    min_layer = -1

    for layer in range(num_layers):
        num_zeros = np.count_nonzero(data[layer] == 0)
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            min_layer = layer

    answer = np.count_nonzero(data[min_layer] == 1) * np.count_nonzero(data[min_layer] == 2)

    print("Part 1: ", answer)
    return

def part2(data):

    layers, height, width = data.shape
    image = np.empty(shape=(height,width),dtype=int)

    for i in range(height):
        for j in range(width):
            layer = 0
            color = data[layer,i,j]
            
            while color == 2:
                layer += 1
                color = data[layer,i,j]

            image[i,j] = color

    print(image)
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day8'), type=str )
    parser.add_argument('--file', default='test2.txt',type=str )
    parser.add_argument('--width', default=2, type=int)
    parser.add_argument('--height', default=2, type=int)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file), args.width, args.height)

    part1(data)

    part2(data)

