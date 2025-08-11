import os
import argparse

class Node:
    '''
    Single node of the tree
    '''
    def __init__(self, name:str) -> None:
        self.parent = None
        self.children = []
        self.name = name

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

    def report_orbit_count(self) -> int:
        '''
        Report the number of direct and indirect orbits of the node's subtree 
        '''

        ##                    ##
        # YOUR CODE GOES HERE! #
        ##                    ## 

        return 

class Tree:
    '''
    Class representing a tree
    '''
    def __init__(self):
        self.nodes = {} #Dict of name:Node()

    def add_node(self, name:str) -> None:
        '''
        Add a new node with a given name
        '''
        newnode = Node(name)
        self.nodes[name] = newnode

    def add_connection(self, parent_name:str, child_name:str) -> None:
        '''
        Add a new connection between parent and child
        '''
        parent_node, child_node = self.nodes[parent_name], self.nodes[child_name]
        parent_node.add_child(child_node)
        child_node.set_parent(parent_node)

    def add_child_node(self, parent_name:str, child_name:str) -> None:
        '''
        Add a new child node to an existing parent in one function
        '''
        self.add_node(child_name) #Creates the new node
        self.add_connection(parent_name, child_name) #Connects parent with child

    def report_orbit_counts(self, start_node_name:str) -> None:
        '''
        Report count of direct and indirect orbits in the entire tree (begining from "start_node_name")
        '''
        ##                    ##
        # YOUR CODE GOES HERE! #
        ##                    ## 

    def buildTree(self, data, parent_name) -> None:
        """
        recursively build the orbit tree
        """
        
        children = data[parent_name] # list of object names that orbit this parent
        for child_name in children:
            self.add_child_node(parent_name,child_name)

            # continue recursively if this child has it's own children
            if child_name in data:
                self.buildTree(data,child_name)
 

def parse_input(path):
    """ 
    read in and parse input data
    returns a dictionary of the form {'object name': [list of objects that orbit it]}
    """
    
    data = {}
    with open(path) as f:
        for l in f: # read each line in the file
            l = l.replace('\n','') # remove end of line character
            l = l.split(')') # split into parent and child object names

            if l[0] in data: # if this parent is already a key in the dictionary
                # add this child object to it's list
                data[l[0]].append(l[1])
            else:
                data[l[0]] = [l[1]]

    return data


def part1(data):
    """
    Count the total number of direct and indirect orbits in your map data

    """

    # build the orbit tree from the input data
    orbit_tree = Tree()
    parent_name = 'COM' 
    orbit_tree.add_node(parent_name)
    orbit_tree.buildTree(data,parent_name)


    # count all orbits

    ##                    ##
    # YOUR CODE GOES HERE! #
    ##                    ## 


    return 

def part2(nodes):

    ##                    ##
    # YOUR CODE GOES HERE! #
    ##                    ## 

    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.path.join(os.curdir,'2019\\Day6'), type=str )
    parser.add_argument('--file', default='test.txt',type=str )

    args = parser.parse_args()

    data = parse_input(os.path.join(args.input_dir,args.file))

    part1(data)

    part2()

