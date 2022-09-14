
from collections import defaultdict
import os
import argparse
from itertools import permutations

def parse_input(path):
    """ read in and parse input data
    returns """
    

    with open(path) as f:
        l = f.read()
        l = l.replace('\n','')
        l = l.split(',')
        data = defaultdict(int)
        for i in range(len(l)):
            data[i] = int(l[i])
            
    return data

def intcode(data,input=None):

    code = data.copy()

    pointer = 0
    relative_base = 0
    output = []
    
    while pointer < len(code):

        value = str(code[pointer])
        opcode = int(value[-2:])
        modes = value[:-2]
        modes = modes.zfill(3)[::-1]

        if opcode == 99:
            break
        elif opcode in [1,2]:
            # get first term
            term1 = getParamValue(modes[0],pointer+1,relative_base,code)

            # get second term
            term2 = getParamValue(modes[1],pointer+2,relative_base,code)

            # get save index
            if modes[2] == '0':
                idx3 = code[pointer+3]
            elif modes[2] == '2':
                idx3 = relative_base + code[pointer+3]
            else:
                print('INVALID MODE FOR SAVING VALUE')

            # compute answer
            if opcode == 1:
                code[idx3] = term1 + term2
            elif opcode == 2:   
                code[idx3] = term1 * term2  

            # incriment instruction pointer            
            pointer += 4

        elif opcode == 3:
            
            # get save index
            if modes[0] == '0':
                idx1 = code[pointer+1]
            elif modes[0] == '2':
                idx1 = relative_base + code[pointer+1]
            else:
                print('INVALID MODE FOR SAVING VALUE')

            code[idx1] = input.pop()
            pointer += 2

        elif opcode == 4:
            # get output
            val = getParamValue(modes[0],pointer+1,relative_base,code)
            output.append(val)
            #print(val)
            pointer += 2

        elif opcode == 5:
            # get True/False
            check = getParamValue(modes[0],pointer+1,relative_base,code)

            if check != 0:
                # set pointer
                pointer = getParamValue(modes[1],pointer+2,relative_base,code)
            else:
                pointer += 3

        elif opcode == 6:
            # get True/False
            check = getParamValue(modes[0],pointer+1,relative_base,code)

            if check == 0:
                # set pointer
                pointer = getParamValue(modes[1],pointer+2,relative_base,code)
            else:
                pointer += 3

        elif opcode == 7:
            # get first parameter
            param1 = getParamValue(modes[0],pointer+1,relative_base,code)

            # get second parameter
            param2 = getParamValue(modes[1],pointer+2,relative_base,code)

            # get save index
            if modes[2] == '0':
                idx1 = code[pointer+3]
            elif modes[2] == '2':
                idx1 = relative_base + code[pointer+3]
            else:
                print('INVALID MODE FOR SAVING VALUE')

            if param1 < param2:
                # store 1
                code[idx1] = 1
            else:
                # store 0
                code[idx1] = 0

            pointer += 4

        elif opcode == 8:
            # get first parameter
            param1 = getParamValue(modes[0],pointer+1,relative_base,code)

            # get second parameter
            param2 = getParamValue(modes[1],pointer+2,relative_base,code)

            # get save index
            if modes[2] == '0':
                idx1 = code[pointer+3]
            elif modes[2] == '2':
                idx1 = relative_base + code[pointer+3]
            else:
                print('INVALID MODE FOR SAVING VALUE')

            if param1 == param2:
                # store 1
                code[idx1] = 1
            else:
                # store 0
                code[idx1] = 0

            pointer += 4

        elif opcode == 9:
            # update relative base
            relative_base += getParamValue(modes[0],pointer+1,relative_base,code)

            pointer += 2

        else:
            print('INVALIDE OPCODE')

    return output

def getParamValue(mode,idx,relative_base,code):

    if mode == '0': # position mode
        return code[code[idx]]

    elif mode == '1': # immediate mode
        return code[idx]

    elif mode == '2': # relative mode
        return code[relative_base + code[idx]]
    else:
        print('INVALID MODE')
        return


def executeSequence(program,sequence,input):

    for i in range(len(sequence)):
        input = intcode(program,[input,sequence[i]])[0]

    return input

def part1(data):

    max_output = 0
    for sequence in permutations([0,1,2,3,4]):
        output = executeSequence(data,sequence,0)
        if output > max_output:
            max_output = output

    print('Part 1: ',max_output)

    return

def part2(data):

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\Day7'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

