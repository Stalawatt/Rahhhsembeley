import sys, re

class DATAMEMORY :
    def __init__(self, length:int):
        """
        
        Data Memory for the program, each index in memory has another array of length 2 that is in format [value, type]
        
        Methods :
        .get_value(index) : returns value at the given index
        .get_type(index) : returns type at the given index
        .set_value(index, value) : if value is of correct type, sets the value at index given to value given

        """
        self.length : int = int(length) # this is the length of the array
        self.__MEMORYARRAY : list[object,type]= [[None,None]] * self.length # generate the array that starts as [None,None] for every index in the array

    def get_value(self, index:int):
        self.__val_index(index)
        return self.__MEMORYARRAY[index]
    
    
    
    def set_value(self, index:int, value:int|str|float):
        self.__val_index(index)

        
        self.__MEMORYARRAY[index] = value
        return
    
    def declare(self, index:int, value:int|str|float):
        self.__val_index(index)
        self.__MEMORYARRAY[index] = value
        return
    
    def __val_index(self, index:int):
        if index > self.length-1:
            return ValueError("Index out of range")
    

class Instr:
    def __init__(self):
        """
        Container class for all the instructions needed for the program :

        ALLOCATE [int]                               Specify the length of and initialise the data array
        DECLARE [index] [value] [type]               Initialise a variable at index, of type, with value
        LOAD [index or value]                        Load data from index (or value) into register
        STORE [index]                                Store data from register into index
        HALT                                         End the program
        JUMP [line number]                           Unconditionally jump to instruction line
        JUMPIF [line number] [condition]             Conditionally jump to instruction line
        ADD [index or value]                         Add value from index (or direct value) to register
        SUB [index or value]                         Subtract value from index (or direct value) to register
        PRINT                                        Print value in register to console

        These 10 instructions make a turing complete machine
        """

        self.data : DATAMEMORY = None
        self.register : int|str|float = None
        self.types = {"int" : int, "str" : str, "float" : float}

    def HALT(self):
        sys.exit(0)

    def ALLOCATE(self,length:int):
        self.data = DATAMEMORY(length)

    def DECLARE(self,index:int,value:str):
        if value.isdigit():
            inferred_value = int(value)
        else:
            try:
                inferred_value = float(value)
            except ValueError:
                inferred_value = value
        self.data.declare(int(index),inferred_value)

    def LOAD_INDEX(self,index:int):
        self.register = self.data.get_value(int(index))
    
    def LOAD_VALUE(self,value:str):
        self.register = value

    def STORE(self, index:int):
        self.data.set_value(int(index),self.register)
    
    def PRINT(self):
        print(self.register)

    def ADD_INDEX(self, index:int):
        self.register += self.data.get_value(int(index))

    def ADD_VALUE(self,value:str):
        self.register += value

    def SUB_INDEX(self, index:int):
        self.register -= self.data.get_value(int(index))

    def SUB_VALUE(self,value:str):
        self.register -= value

    def JUMPIF(self, index : int, condition:str):
        pattern = r"&(\d+)"
        def replace_memory(match):
            variable = int(match.group(1))
            return str(self.data.get_value(variable))
        if eval(re.sub(pattern,replace_memory,condition)):
            interpreter.currentline = int(index)-2


class Parser:
    def __init__(self):
        """
        Parser for interpreting each line and what to do
        """
        self.instructions = Instr()
        

    def parseLine(self,line:str):
        if "#" in line:
            return
        line = line.rstrip("\n")
        if " " in line:

            line = line.split()
            match line[0]:
                case "ALLOCATE":
                    self.instructions.ALLOCATE(line[1])
                case "DECLARE":
                    self.instructions.DECLARE(line[1],line[2])
                case "LOAD":
                    if "&" in line[1]:
                        self.instructions.LOAD_INDEX(line[1].lstrip("&"))
                    else:
                        self.instructions.LOAD_VALUE(line[1])
                case "STORE":
                    self.instructions.STORE(line[1])
                case "ADD":
                    if "&" in line[1]:
                        self.instructions.ADD_INDEX(line[1].lstrip("&"))
                    else:
                        self.instructions.ADD_VALUE(line[1])
                case "SUB":
                    if "&" in line[1]:
                        self.instructions.SUB_INDEX(line[1].lstrip("&"))
                    else:
                        self.instructions.SUB_VALUE(line[1])
                case "JUMP":
                    interpreter.currentline = int(line[1])-2
                
                case "JUMPIF" :
                    self.instructions.JUMPIF(line[1], "".join(line[1:]))

                    

                
        else :
            match line:
                case "HALT" :
                    self.instructions.HALT()
                case "PRINT" :
                    self.instructions.PRINT()

            


class Interpreter:
    def __init__(self,file):
        self.file = list(file)
        self.currentline = 0
        self.parser = Parser()
        

    def nextLine(self):
        self.parser.parseLine(self.file[self.currentline])
        self.currentline += 1
        

def begin_program(file):
    global interpreter
    interpreter = Interpreter(file)
    while True:
        interpreter.nextLine()