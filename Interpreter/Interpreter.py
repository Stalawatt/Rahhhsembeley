import sys

class DATAMEMORY :
    def __init__(self, length:int):
        """
        
        Data Memory for the program, each index in memory has another array of length 2 that is in format [value, type]
        
        Methods :
        .get_value(index) : returns value at the given index
        .get_type(index) : returns type at the given index
        .set_value(index, value) : if value is of correct type, sets the value at index given to value given

        """
        self.length : int = length # this is the length of the array
        self.__MEMORYARRAY : list[object,type]= [[None,None]] * length # generate the array that starts as [None,None] for every index in the array

    def get_value(self, index:int):
        self.__val_index(index)
        return self.__MEMORYARRAY[index][0]
    
    def get_type(self, index:int):
        self.__val_index(index)
        return self.__MEMORYARRAY[index][1]
    
    def set_value(self, index:int, value:int|str|float):
        self.__val_index(index)
        if type(value) != self.__MEMORYARRAY[index][1]: # static types 
            raise TypeError("Cannot change datatype")
        
        self.__MEMORYARRAY[index][0] = value
        return
    
    def declare(self, index:int, value:int|str|float, type:type):
        self.__val_index(index)
        self.__MEMORYARRAY[index] = [type(value),type]
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

    def HALT(self):
        sys.exit(0)

    def ALLOCATE(self,length:int):
        self.data = DATAMEMORY(length)

    def DECLARE(self,index:int,value:int|str|float, type:type):
        self.data.declare(index,value,type)

    def LOAD_INDEX(self,index:int):
        self.register = self.data.get_value(index)
    
    def LOAD_VALUE(self,value:int|str|float):
        self.register = value

    def STORE(self, index:int):
        self.data.set_value(index,self.register)
    
    def PRINT(self):
        print(self.register)

    def ADD_INDEX(self, index:int):
        self.register += self.data.get_value(index)

    def ADD_VALUE(self,value:int|str|float):
        self.register += value

    def SUB_INDEX(self, index:int):
        self.register -= self.data.get_value(index)

    def SUB_VALUE(self,value:int|str|float):
        self.register -= value