import os
import argparse
import time

def parse_input(path):
    """ read in and parse input data
    returns """
    
    numbers = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split(',')
            l = [int(x) for x in l]
            numbers += l  

    return numbers


def play_game(data,num_turns):
    turn = 0
    history = {x:[] for x in data}

    for num in data:
        turn += 1
        history[num].append(turn)

    while turn < num_turns:
        if len(history[num]) == 2:
            new_num = history[num][1] - history[num][0]
            history[num].pop(0)
        else:
            new_num = 0

        turn += 1
        if new_num in history:
            history[new_num].append(turn)    
        else:
            history[new_num] = [turn]
        num = new_num    

    return num


def part1(data):
    
    start = time.time()
    num = play_game(data,2020)
    print(num)
    end = time.time()
    print('part 1 time: {t}'.format(t=end-start))
    
    return

def part2(data):

    start = time.time()
    num = play_game(data,30000000)
    print(num)
    end = time.time()
    print('part 2 time: {t}'.format(t=end-start))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day15'), type=str, help=f'''''')
    parser.add_argument('--file', default='test1.txt',type=str, help=f'''''')

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

