from collections import defaultdict
from collections import Counter
import datetime
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    with open(path) as f:
        puzzle_input = f.read().splitlines()
        puzzle_input = sorted(puzzle_input)

    
    data = defaultdict(list)
    for row in puzzle_input:

        row = row.replace('\n','')
        row = row.replace("[","").replace("] ",",").replace("Guard #",'')
        row = row.split(",")
        date = datetime.datetime.strptime(row[0],'%Y-%m-%d %H:%M')
        row = row[1].split(" ")
        if len(row) == 3:
            guard = row[0]
            action = ' '.join(row[1:])
        else:
            action = ' '.join(row)

        data[guard].append((date,action)) 

    
    return data


def countSleep(data):

    sleep_counter = {}
    for guard, log in data.items():
        guard_sleep_counter = Counter()

        asleep = False
        for (time, action) in log:
            if action == 'falls asleep':
                assert asleep == False
                sleep_min = time.minute
                asleep = True
            elif action == 'wakes up':
                assert asleep == True
                wake_min = time.minute
                asleep = False
                guard_sleep_counter.update(range(sleep_min,wake_min))

        sleep_counter[guard] = guard_sleep_counter

    return sleep_counter


def part1(sleep_counter):

    total_sleep = {guard:sum(counter.values()) for guard, counter in sleep_counter.items()}
    sleepiest_guard = max(total_sleep,key=total_sleep.get)
    sleepiest_min, __ = sleep_counter[sleepiest_guard].most_common()[0]
    soln = int(sleepiest_guard) * sleepiest_min
    print("Part 1: {t}".format(t=soln))
    return

def part2(sleep_counter):

    max_sleep_count = 0

    for guard, counter in sleep_counter.items():
        
        if len(counter) == 0: # skip sleepless guard
            continue

        guard_max_sleep_count = counter[max(counter,key=counter.get)]
        if guard_max_sleep_count > max_sleep_count:
            max_sleep_count = guard_max_sleep_count
            sleepiest_guard = guard
            sleepiest_minute = max(counter,key=counter.get)


    print("Part 2: {x}".format(x=int(sleepiest_guard) * sleepiest_minute))

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2018\Day4'), type=str)
    parser.add_argument('--file', default='input.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    sleep_counter = countSleep(data)

    part1(sleep_counter)

    part2(sleep_counter)

