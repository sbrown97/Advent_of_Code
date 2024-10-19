import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        l = f.read()
        l = l.replace('\n','')
        l = l.split(',')
        data = [int(x) for x in l]
        
    return data

def intcode(data,input):

    code = data.copy()

    pointer = 0
    
    while pointer < len(code):

        value = str(code[pointer])
        opcode = int(value[-2:])
        modes = value[:-2]

        if opcode == 99:
            break
        elif opcode in [1,2]:
            modes = modes.zfill(3)[::-1]

            # get first term
            if modes[0] == '1':
                term1 = code[pointer+1]
            else:
                term1 = code[code[pointer+1]]

            # get second term
            if modes[1] == '1':
                term2 = code[pointer+2]
            else:
                term2 = code[code[pointer+2]]

            # compute answer
            idx3 = code[pointer+3]
            if opcode == 1:
                code[idx3] = term1 + term2
            elif opcode == 2:   
                code[idx3] = term1 * term2  

            # incriment instruction pointer            
            pointer += 4

        elif opcode == 3:
            idx1 = code[pointer+1]
            code[idx1] = input
            pointer += 2

        elif opcode == 4:
            modes = modes.zfill(1)[::-1]

            # get output
            if modes[0] == '1':
                output = code[pointer+1]
            else:
                output = code[code[pointer+1]]

            print(output)
            pointer += 2

        elif opcode == 5:
            modes = modes.zfill(2)[::-1]

            # get True/False
            if modes[0] == '1':
                check = code[pointer+1]
            else:
                check = code[code[pointer+1]]

            if check != 0:
                # set pointer
                if modes[1] == '1':
                    pointer = code[pointer+2]
                else:
                    pointer = code[code[pointer+2]]
            else:
                pointer += 3

        elif opcode == 6:
            modes = modes.zfill(2)[::-1]

            # get True/False
            if modes[0] == '1':
                check = code[pointer+1]
            else:
                check = code[code[pointer+1]]

            if check == 0:
                # set pointer
                if modes[1] == '1':
                    pointer = code[pointer+2]
                else:
                    pointer = code[code[pointer+2]]
            else:
                pointer += 3

        elif opcode == 7:
            modes = modes.zfill(3)[::-1]

            # get first parameter
            if modes[0] == '1':
                param1 = code[pointer+1]
            else:
                param1 = code[code[pointer+1]]

            # get second parameter
            if modes[1] == '1':
                param2 = code[pointer+2]
            else:
                param2 = code[code[pointer+2]]

            if param1 < param2:
                # store 1
                code[code[pointer+3]] = 1
            else:
                # store 0
                code[code[pointer+3]] = 0

            pointer += 4

        elif opcode == 8:
            modes = modes.zfill(3)[::-1]

            # get first parameter
            if modes[0] == '1':
                param1 = code[pointer+1]
            else:
                param1 = code[code[pointer+1]]

            # get second parameter
            if modes[1] == '1':
                param2 = code[pointer+2]
            else:
                param2 = code[code[pointer+2]]

            if param1 == param2:
                # store 1
                code[code[pointer+3]] = 1
            else:
                # store 0
                code[code[pointer+3]] = 0

            pointer += 4

        else:
            print('INVALIDE OPCODE')

    return code[0]

def part1(data):

    intcode(data,1)

    return

def part2(data):
    #code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    #intcode(code,0)
    intcode(data,5)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day5'), type=str )
    parser.add_argument('--file', default='input.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

