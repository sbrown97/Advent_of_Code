import os
import argparse

class Node:
    '''
    Single node of the tree
    '''
    def __init__(self, name:str, file_size:int) -> None:
        self.parent = None
        self.children = []
        self.name = name
        self.file_size = file_size

    def set_parent(self, other_node) -> None:
        '''
        Set the node's parent
        '''
        self.parent = other_node
    
    def add_child(self, other_node) -> None:
        '''
        Add a child node
        '''
        self.children.append(other_node)


class Tree:
    '''
    Class representing a tree
    '''
    def __init__(self):
        self.nodes = {} #Dict of name:Node()
        self.directories = {} 

    def print_node_names(self):
        for node in self.nodes:
            print(node)

    def add_node(self, name:str, file_size:str) -> None:
        '''
        Add a new node with a given name
        '''
        if file_size == 'dir':
            newnode = Node(name,0)
            self.nodes[name] = newnode
            self.directories[name] = newnode
        else:
            newnode = Node(name,int(file_size))
            self.nodes[name] = newnode

    def add_connection(self, parent_name:str, child_name:str) -> None:
        '''
        Add a new connection between parent and child
        '''
        parent_node, child_node = self.nodes[parent_name], self.nodes[child_name]
        parent_node.add_child(child_node)
        child_node.set_parent(parent_node)

    def add_child_node(self, parent_name:str, child_name:str, child_size:int) -> None:
        '''
        Add a new child node to an existing parent in one function
        '''
        self.add_node(child_name, child_size) #Creates the new node
        self.add_connection(parent_name, child_name) #Connects parent with child

    def report_file_sizes(self, start_node_name:str) -> None:
        '''
        Report total file size of the tree (begining from "start_node_name")
        '''
        files_to_visit = [self.nodes[start_node_name]]
        size = 0
        while len(files_to_visit) > 0:
            current_node = files_to_visit.pop()
            size += current_node.file_size
            files_to_visit += current_node.children

        return size

    def report_dir_sizes(self):
        '''
        report the size of every directory in the file tree
        '''

        dir_sizes = {}
        for dir in self.directories:
            size = self.report_file_sizes(dir)
            dir_sizes[dir] = size

        return dir_sizes

 

def parse_input(path):
    """ 
    read in and parse input data 
    builds tree as you go
    """
    
    cur_dir = ''
    fileTree = Tree()
    fileTree.add_node('/','dir')

    commands = set()
    with open(path) as f:
        for l in f: # read each line in the file
            l = l.replace('\n','') # remove end of line character

            if l[0] == '$': 
                commands.add(l.split(' ')[1])
                if 'cd' in l: # update current directory
                    cmd = l.split(' ')[-1]
                    if cmd == '..': # move out one level
                        cur_dir = '_'.join(cur_dir.split('_')[:-1])
                    else:
                        cur_dir = '_'.join([cur_dir,cmd]) if len(cur_dir) > 0 else cmd
                else:
                    continue

            else: 
                l = l.split(' ')
                name = cur_dir + '_' + l[1]

                if name == 'jllhmmf':
                    print(l)
                size = l[0]
                fileTree.add_child_node(cur_dir,name,size)
                
           
    return fileTree


def part1(fileTree):
    """
    Count the total number of direct and indirect orbits in your map data

    """

    dir_sizes = fileTree.report_dir_sizes()
    total_size = 0
    for dir in dir_sizes:
        if dir_sizes[dir] <= 100000:
            total_size += dir_sizes[dir]


    print(total_size)


    return 


def part2(fileTree):

    ram = 70000000
    required_space = 30000000

    used_space = fileTree.report_file_sizes('/')
    unused_space = ram - used_space
    
    dir_sizes = fileTree.report_dir_sizes()

    min_dir = '/'
    min_dir_size = dir_sizes[min_dir]
    for dir, size in dir_sizes.items():
        if (size >= required_space - unused_space) & (size < min_dir_size):
            min_dir = dir
            min_dir_size = size

    print(min_dir, min_dir_size)

    return 


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2022\\Day7'), type=str)
    parser.add_argument('--file', default='test.txt',type=str)

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2(data)

