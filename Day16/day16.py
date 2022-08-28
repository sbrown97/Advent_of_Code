import numpy as np
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    tickets = []
    rules = {}
    with open(path) as f:
        parsing_rules = True
        my_ticket = False
        nearby_tickets = False
        for l in f:
            l = l.replace('\n','')
            if len(l) == 0:
                parsing_rules = False
                continue
            elif l == 'your ticket:':
                my_ticket = True
                continue
            elif l == 'nearby tickets:':
                nearby_tickets = True
                my_ticket = False
                continue
            
            if parsing_rules:
                l = l.split(': ')
                rules[l[0]] = l[1]
            elif my_ticket:
                ticket = [int(x) for x in l.split(',')]
            elif nearby_tickets:
                tickets.append([int(x) for x in l.split(',')])

        rules = parse_rules(rules)

    return rules, ticket, tickets


def parse_rules(rules):

    for key,value in rules.items():
        value = value.split(' or ')
        allowed = set()
        for v in value:
            v = v.split('-')
            for i in range(int(v[0]),int(v[1]) + 1):
                allowed.add(i)
        rules[key] = allowed

    return rules


def part1(rules,tickets):

    full_set = set()
    for key,value in rules.items():
        full_set = full_set.union(value)

    total = 0
    good_tickets = []
    for i in range(len(tickets)):
        nums = set(tickets[i])
        dif = nums.difference(full_set)
        if len(dif) > 0:
            total += sum(dif)
        else:
            good_tickets.append(tickets[i])        

    print(total)

    return good_tickets


def determine_fields(rules,tickets):

    tickets = np.array(tickets)

    num_fields = tickets.shape[1]
    fields = {}
    option_counter = {key:0 for key in rules.keys()}

    for i in range(num_fields):
        entries = set(tickets[:,i])
        for field, values in rules.items():
            dif = entries.difference(values)
            if len(dif) == 0:
                option_counter[field] += 1
                if field in fields:
                    fields[field].append(i)
                else:
                    fields[field] = [i]

    while sum(option_counter.values()) > 0:
        field = min(option_counter,key=option_counter.get)
        i = fields[field][0]
        for key in option_counter.keys():
            if i in fields[key]:
                fields[key].remove(i)
                option_counter[key] -= 1

        fields[field] = i
        option_counter.pop(field)

    return fields


def part2(rules,ticket,tickets):

    fields = determine_fields(rules,tickets)

    answer = 1
    for key,idx in fields.items():
        if key.startswith('departure'):
            answer *= ticket[idx]

    print(answer)
    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day16'), type=str, help=f'''''')
    parser.add_argument('--file', default='test2.txt',type=str, help=f'''''')

    args = parser.parse_args()

    rules, ticket, tickets = parse_input(os.path.join(args.input_dir,args.file))

    good_tickets = part1(rules,tickets)

    part2(rules,ticket,good_tickets)

