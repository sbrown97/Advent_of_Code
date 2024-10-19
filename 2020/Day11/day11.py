import numpy as np
import pandas as pd
import os
import argparse

def parse_input(path):
    """ read in and parse input data
    returns """
    
    data = []
    with open(path) as f:
        for l in f:
            l = l.replace('\n','')
            # 0 = floor, -1 = empty seat, 1 = occupied seat
            row = [0 if x == '.' else -1 for x in l]
            
            data.append(row)  

    return np.array(data)


def update_seats(seats):

    num_changes = 0

    new_seats = seats.copy()
    (num_rows,num_cols) = seats.shape

    x, y = np.where(seats!=0) # don't bother checking floor spaces

    for (row,col) in zip(x,y):
        min_row = max(row-1,0)
        max_row = min(row+2,num_rows)
        min_col = max(col-1,0)
        max_col = min(col+2,num_cols)

        # check empty seats
        if (seats[row,col] == -1) and (sum(sum(seats[min_row:max_row,min_col:max_col] <= 0)) == seats[min_row:max_row,min_col:max_col].size):
            new_seats[row,col] = 1
            num_changes += 1
        # check occupied seats
        if (seats[row,col] == 1) and (sum(sum(seats[min_row:max_row,min_col:max_col] == 1)) > 4):
            new_seats[row,col] = -1
            num_changes += 1

    return new_seats, num_changes


def part1(data):
    
    seats = data.copy()
    num_changes = 1 # dummy initialization to get into while loop

    while num_changes > 0:
        seats, num_changes = update_seats(seats)

    occupied_seats = seats[seats == 1].size

    print(occupied_seats)
    return


def get_visible_seats(data,i,j):
    visible = []
    (num_rows,num_cols) = data.shape

    # N
    if i > 0:
        seats = np.flip(data[0:i,j])
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])


    # NE
    if (i > 0) and (j + 1 < num_cols):
        size = min(i,num_cols - j - 1)
        seats = np.flip(np.fliplr(data[i-size:i,j+1:j+size+1])).diagonal()
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # E
    if j + 1 < num_cols:
        seats = data[i,j+1:]
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # SE
    if (i + 1 < num_rows) and (j + 1 < num_cols):
        seats = data[i+1:num_rows,j+1:num_cols].diagonal()
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # S
    if i + 1 < num_rows:
        seats = data[i+1:,j]
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # SW
    if (i + 1 < num_rows) and (j > 0):
        seats = np.fliplr(data[i+1:num_rows,0:j]).diagonal()
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # W
    if j > 0:
        seats = np.flip(data[i,0:j])
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    # NW
    if (i > 0) and (j > 0):
        size = min(i,j)
        seats = np.flip(data[i-size:i,j-size:j].diagonal())
        # add the first visible seat to the list
        if len(seats[seats!=0]) > 0:
            visible.append(seats[seats!=0][0])

    return np.array(visible)


def part2(data):

    num_changes = 1 # dummy initialization to get into while loop
    

    while num_changes > 0:
        num_changes = 0
        new_data = data.copy()

        x, y = np.where(data!=0) # don't bother checking floor spaces

        for (row,col) in zip(x,y):
            # get list of visible seats
            visible = get_visible_seats(data,row,col)

            # check empty seats
            if (data[row,col] == -1) and (1 not in visible):
                new_data[row,col] = 1
                num_changes += 1
            # check occupied seats
            if (data[row,col] == 1) and (np.count_nonzero(visible == 1) >= 5):
                new_data[row,col] = -1
                num_changes += 1

        data = new_data

    occupied_seats = new_data[new_data == 1].size

    print(occupied_seats)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'Day11'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

