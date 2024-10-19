import os
import argparse
import re

def parse_input(path):
    """ read in and parse input data
    return list of dictionaries"""

    data = []
    with open(path) as f:
        passport = {}
        for l in f:
            l = l.replace('\n','')
            
            if len(l):
                l = l.split()
                for phrase in l:
                    [key,value] = phrase.split(':')
                    passport[key] = value
            else:
                data.append(passport)
                passport = {}

        data.append(passport)
    return data


def fields_present(fields,passport):
    """check that the passport contains all of the required fields"""

    return fields.issubset(passport.keys())

    
def fields_valid(passport):

    # byr must be a number between 1920 and 2002
    try:
        byr = int(passport['byr'])
        if 1920 > byr or byr > 2002:
            #print('byr out of range: {byr}'.format(byr=byr))
            return False  
    except:
        #print('invalid byr: {byr}'.format(byr=passport['byr']))
        return False

    # iyr must be a number between 2010 and 2020
    try: 
        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            #print('iyr out of range: {iyr}').format(iyr=iyr)
            return False
    except:
        #print('invalid iyr: {iyr}'.format(iyr=passport['iyr']))
        return False

    # eyr must be a number between 2020 and 2030
    try:
        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            #print('eyr out of range: {eyr}'.format(eyr=eyr))
            return False
    except:
        #print('invalid eyr: {eyr}'.format(eyr=passport['eyr']))
        return False

    # hgt must be a number followed either 'cm' or 'in'
    try:
        height = int(passport['hgt'][:-2])
        units = passport['hgt'][-2:]

        if units == 'cm':
            # if the units are cm, height must be between 150 and 193
            if height < 150 or height > 193:
                #print('height out of range for cm: {height}'.format(height=height))
                return False
        elif units == 'in':
            # if the units are in, height must be between 59 and 76
            if height < 59 or height > 76:
                #print('height out of range for in: {height}'.format(height=height))
                return False
        else:
            #print('invalid height units: {units}'.format(units=units))
            return False
    except:
        #print('invalid height number: {hgt}'.format(hgt=passport['hgt']))
        return False

    # hcm must be a '#' followed by 6 characters in 0-9 or a-f
    hcl = passport['hcl']
    if hcl[0] != '#':
        #print('hcl does not start with #: {hcl}'.format(hcl=hcl))
        return False
    elif len(re.findall("[0-9a-f]{6}", hcl[1:])) == 0:
        #print('invalid hcl chars/length: {hcl}'.format(hcl=hcl[1:]))
        return False

    # ecl must be one of the following colors
    colors = set(['amb','blu','brn','gry','grn','hzl','oth'])
    if passport['ecl'] not in colors:
        #print('ecl not in colors: {ecl}'.format(ecl=passport['ecl']))
        return False

    # pid must be a 9 digit number, including leading zeros
    if len(passport['pid']) == 9:
        try:
            int(passport['pid'])
        except:
            #print('pid not a number: {pid}'.format(pid=passport['pid']))
            return False
    else:
        #print('pid not 9 characters: {pid}'.format(pid=passport['pid']))
        return False

    return True


def part1(data):
    # required fields
    fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    num_valid = 0

    # check each passport for required fields
    for passport in data:
        if fields_present(fields,passport):
            num_valid += 1

    print(num_valid)
    return


def part2(data):
    fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    num_valid = 0

    for passport in data:
        # check for required fields
        if fields_present(fields,passport):
            # check that all values are valid
            if fields_valid(passport):
                num_valid += 1

    print(num_valid)

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day4'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    passports = parse_input(os.path.join(args.input_dir,args.file))

    part1(passports)

    part2(passports)