
class Intcoder():
    def __init__(self, program):
        """store program and initialize useful data"""

        # store the original program as well as a copy that will be updated as the program executes
        self.original_program = program.copy()
        self.program = program.copy()

        # initialize pointer value
        self.pointer = 0
        # initialize relative base value
        self.relative_base = 0

        # the number of parameters for each opcode
        self.num_params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0}

        # initialize empty input list
        self.input = []

        # initialize empty output list
        self.output = []

        # initilize status (1 = ready to run, 0 = finished, -1 = output generated)
        self.status = 1

    def reset(self):
        '''reset everything back to initalization'''
        self.program = self.original_program.copy()
        self.pointer = 0
        self.relative_base = 0
        self.input = []
        self.output = []
        self.status = 1

    def provide_input(self,input):
        # append the new input to the beginning of the input list
        if type(input) == list:
            input.reverse()
            self.input = input + self.input
        else:
            self.input = [input] + self.input

    def get_output(self):
        return self.output.pop()

    def execute_opcode(self) -> int:
        """execute the next instruction"""
        
        
        opcode = self.program[self.pointer] % 100
        modes = str(self.program[self.pointer])[:-2]
        modes = modes.zfill(3)[::-1]

        if opcode == 99:
            return 0
        else:
            # get all parameters
            addresses = [self.getAddress(modes[x], self.pointer + x + 1) for x in range(self.num_params[opcode])]

            if opcode == 1: # sum
                self.program[addresses[2]] = self.program[addresses[0]] + self.program[addresses[1]]
                self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 2: # multiply
                self.program[addresses[2]] = self.program[addresses[0]] * self.program[addresses[1]]
                self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 3: # input
                self.program[addresses[0]] = self.input.pop()
                self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 4: #output
                # save output to the beginning of the output list
                self.output = [self.program[addresses[0]]] + self.output
                self.pointer += self.num_params[opcode] + 1
                return -1
            
            elif opcode == 5: # jump if true
                if self.program[addresses[0]] != 0:
                    self.pointer = self.program[addresses[1]]
                else:
                    self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 6: # jump if false
                if self.program[addresses[0]] == 0:
                    self.pointer = self.program[addresses[1]]
                else:
                    self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 7: # less than
                if self.program[addresses[0]] < self.program[addresses[1]]:
                    self.program[addresses[2]] = 1
                else:
                    self.program[addresses[2]] = 0
                self.pointer += self.num_params[opcode] + 1
            
            elif opcode == 8: #equal to
                if self.program[addresses[0]] == self.program[addresses[1]]:
                    self.program[addresses[2]] = 1
                else:
                    self.program[addresses[2]] = 1
                self.pointer += self.num_params[opcode] + 1

            elif opcode == 9: # update relative base
                self.relative_base += self.program[addresses[0]]
                self.pointer += self.num_params[opcode] + 1

            return 1


    def getAddress(self,mode,idx):

        if mode == '0': # position mode
            return self.program[idx]

        elif mode == '1': # immediate mode
            return idx

        elif mode == '2': # relative mode
            return self.relative_base + self.program[idx]
        else:
            print('INVALID MODE')
            return

    def run(self):
        '''executes the program until an output is generated or the program terminates'''

        #TODO: make sure it is safe to restart
        self.status = 1
        
        while self.status == 1:
            self.status = self.execute_opcode()