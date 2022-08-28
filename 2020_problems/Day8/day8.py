import os
import argparse
import pandas as pd

def parse_input(path):
    """read and parse input data
    returns dataframe with instructions and value"""

    data = pd.DataFrame(columns=['instruction','value'])

    with open(path) as f:
        for l in f:
            l = l.split()
            inst = l[0]
            value = int(l[1])
            data = data.append({'instruction':inst,'value':value},ignore_index=True)

    return data


def execute_instructions(data):

    # track instructions visited, accumulator value, and current instruction
    visited = set()
    accumulator = 0
    idx = 0

    # execute instructions until reach the end or hit an endless loop
    while (idx not in visited) and (idx < len(data)):
        visited.add(idx)
        operator = data.loc[idx,'instruction']
        value = data.loc[idx,'value']

        if operator == 'acc': # increment the accumulator
            accumulator += value
            idx += 1
        elif operator == 'jmp': # jump to another instruction
            idx += value
        elif operator == 'nop': # do nothing
            idx += 1

    successfull = idx == len(data)
    return accumulator, successfull
    

def part1(data):
    accumulator, _ = execute_instructions(data)
    print(accumulator)
    return


def part2(data):
    
    swap = {'nop':'jmp','jmp':'nop'}
    
    # try swaping each jmp/nop instruction until the program finishes successfully
    for row in data.itertuples():
        test_data = data.copy()

        if row.instruction in ['nop','jmp']:
            test_data.loc[row.Index,'instruction'] = swap[row.instruction]
            accumulator, success = execute_instructions(test_data)
            if success:
                print(accumulator)
                return

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day8'), type=str, help=f'''''')
    parser.add_argument('--file', default='test.txt',type=str, help=f'''''')

    args = parser.parse_args()

    program = parse_input(os.path.join(args.input_dir,args.file))

    part1(program)

    part2(program)

    