import string
import os
import argparse
from PIL import Image

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path,encoding = 'utf-8') as f:
        for l in f:
            l = l.strip('\n')
            data.append(l)

    return ''.join(data)


def part1(data):

    punctuaion = '.?!c;:'
    spaces = []
    indices = []
    for i, c in enumerate(data):
        if c in string.punctuation:
            indices.append(i)
    
    for i in indices:
        if data[i+1]==' ':
            spaces.append(data[i+1:i+3].count(' ')-1)

    code = ''.join(map(str,spaces))
    code = [chr(int(code[i:i+8],2)) for i in range(0,len(code),8)]
    
    print(f'part 1: {''.join(code)}')
    return

def part2(data):

    sections = data.split('0xdeadbeef')

    code = ['0' if i.islower() else '1' for i in sections[1] if i.isalpha()]
    code = ''.join(code)

    num_chars = int(len(code)/16)
    code = [chr(int(code[i:i+num_chars],2)) for i in range(0,len(code),num_chars)]

    print(f'part 2: {''.join(code)}')

    return 

def challenge(path):

    img = Image.open(path)
    pixels = list(img.getdata())
    LSBs = ''

    for p in pixels:
        LSBs += bin(p & 1)[2:].zfill(1)

    for offset in range(8):
        text = ''.join([chr(int(LSBs[i+offset:i+offset+8],2)) for i in range(0,len(LSBs[offset:]),8)])
        text = text.split('0xdeadbeef')
        if len(text) == 3:
            message = text[1]
            print(f'challenge: {message}')
            return

    print('no message found') 
    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'week5'), type=str)
    parser.add_argument('--file1', default='week5_part1_message.txt',type=str)
    parser.add_argument('--file2', default='week5_part2_document.txt',type=str)
    parser.add_argument('--file3', default='week5_security_cam.png',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file1))

    part1(data)
    
    data = parse_input(os.path.join(args.input_dir,args.file2))

    part2(data)

    challenge(os.path.join(args.input_dir,args.file3))


