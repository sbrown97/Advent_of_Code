import os
import argparse


def parse_input(path):
    """ read in and parse input data
    returns a dict of dicts (e.g., {'red': {'white' 1, 'yellow': 2}} )"""
    
    data = {}
    with open(path) as f:   
        for l in f:
            l = l.replace('\n','')
            l = l.replace('bags','bag')
            l = l.split('bag')
            # the first bag mentioned is the main bag of this rule
            main_bag = l[0].strip() 
            bags = {}

            # build inner dictionary for the bags contained within the main bag
            for b in l[1:-1]:
                b = b.replace('contain','')
                b = b.replace(',','')
                b = b.strip()
                if 'no other' not in b:
                    bags[b[2:]] = int(b[0])
            data[main_bag] = bags

    return data


def check_next_level(color,data,bag):
    '''Recursive function to check whether the specific color bag is contained in a bag'''
    
    inner_bags = data[bag]
    if len(inner_bags) > 0:
        for bag in inner_bags.keys():
            if bag == color: # stop if color is found
                return True
            else:
                # continue looking
                if check_next_level(color,data,bag):
                    return True
    else:
        # stop if no more inner bags to check
        return False


def part1(data,color='shiny gold'):

    counter = 0

    # Check each bag type
    for bag, __ in data.items():
        # does this bag contain the desired color?
        contains_color = check_next_level(color,data,bag)
        if contains_color:
            # if yes, increase the counter
            counter += 1

    print(counter)

    return


def count_bags(color,data):
    '''Recursive function to count the number of bags contained within a bag'''

    count = 0
    
    if len(data[color]) == 0:
        # stop if this color doesn't contain any other bags
        return count

    # check each inner bag
    for (c,num) in data[color].items(): 
        # add the number of bags c contained in bag color and all of the bags within it
        count += num + num * count_bags(c,data)

    return count


def part2(data):

    color = 'shiny gold'

    # get the total number of bags contained in a shiny gold bag
    num_bags = count_bags(color,data)
    print(num_bags)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day7'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

