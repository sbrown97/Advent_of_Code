import os
import argparse
from copy import deepcopy


class Monkey:

    def __init__(self,name,items,operation,test) -> None:
        self.name = name
        self.items = items 
        self.operation = operation
        self.test = test
        self.num_inspections = 0
        
    def set_true_monkey(self, true_monkey) -> None:
        self.true_monkey = true_monkey
        
    def set_false_monkey(self, false_monkey) -> None:
        self.false_monkey = false_monkey

    def add_item(self,item) -> None:
        self.items.append(item)

    def inspect(self) -> None:
        for i in range(len(self.items)):
            self.num_inspections += 1
            worry = self.items.pop(0)
            operation = self.operation.replace('old',str(worry))
            worry = eval(operation)
            worry = worry // 3
            if worry % self.test == 0:
                self.true_monkey.add_item(worry)
            else:
                self.false_monkey.add_item(worry)
    
    def modulo_inspect(self,modulo) -> None:
        for i in range(len(self.items)):
            self.num_inspections += 1
            worry = self.items.pop(0)
            operation = self.operation.replace('old',str(worry))
            worry = eval(operation)
            worry = worry % modulo
            if worry % self.test == 0:
                self.true_monkey.add_item(worry)
            else:
                self.false_monkey.add_item(worry)

def parse_input(path):
    """ read in and parse input data
    returns """
    
    monkeys = []
    true_monkeys = []
    false_monkeys = []
    row = 0
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')

            if l == '':
                row = 0
                m = Monkey(name,items,operation,test)
                monkeys.append(m)
                continue
            else:
                row += 1

            if row == 1:
                name = int(l.split(' ')[1].replace(':',''))
            elif row == 2:
                items = [int(i) for i in l.split(':')[-1].split(',')]
            elif row == 3:
                operation = l.split(':')[-1].split('=')[-1]
            elif row == 4:
                test = int(l.split(' ')[-1])
            elif row == 5:
                true_monkeys.append(int(l.split(' ')[-1]))
            elif row == 6:
                false_monkeys.append(int(l.split(' ')[-1]))
            else:
                print('Something went wrong parsing input')

    
    m = Monkey(name,items,operation,test)
    monkeys.append(m)
            
    for monkey in monkeys:
        name = monkey.name
        monkey.set_true_monkey(monkeys[true_monkeys[name]])
        monkey.set_false_monkey(monkeys[false_monkeys[name]]) 

    return monkeys


def part1(data):
    monkeys = deepcopy(data)

    for round in range(20):    
        for monkey in monkeys:
            monkey.inspect()

    inspections = sorted([m.num_inspections for m in monkeys],reverse=True)
    monkey_business = inspections[0] * inspections[1]
    print(monkey_business)

    return

def part2(data):
    monkeys = deepcopy(data)
    modulo = 1
    for m in monkeys:
        modulo *= m.test

    for round in range(10000):
        for monkey in monkeys:
            monkey.modulo_inspect(modulo)

    inspections = sorted([m.num_inspections for m in monkeys],reverse=True)
    monkey_business = inspections[0] * inspections[1]
    print(monkey_business)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\Day11'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

