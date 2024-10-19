import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = pd.read_csv(path,header=None,names=['operation','value'],sep=' ')

    return data


def part1(data):

    data = data.fillna(0)
    data['X'] = data.value.cumsum()
    data['X'] += 1
    
    data['cycle'] = 0 # the cycle column indicates the END of the cycle in which X takes on this row's value

    cycle = 0
    for row in data.itertuples():
        if row.operation == 'noop':
            cycle += 1
        elif row.operation == 'addx':
            cycle += 2
        else:
            print('INVALID OPERATION')

        data.loc[row.Index,'cycle'] = cycle
    
    answer = 0
    for i in range(20,221,40):
        value = data[data.cycle < i][['X']].iloc[-1][0]
        answer += i * value

    print(answer)

    return data

def part2(data):

    image = np.array(['.']*6*40)
    init = pd.DataFrame({'operation':'init','value':0,'X':1,'cycle':-1},index=[0])
    data = pd.concat([init,data]).reset_index(drop=True)

    for cycle in range(6*40):
        pixel = cycle % 40
        sprite = data[data.cycle < cycle + 1][['X']].iloc[-1][0]
        if abs(sprite - pixel) <= 1:
            image[cycle] = '#'
    
    image = image.reshape([6,40])
    np.set_printoptions(linewidth=np.inf)
    print(image)



    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\\Day10'), type=str)
    parser.add_argument('--file', default='test2.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    data = part1(data)

    part2(data)

