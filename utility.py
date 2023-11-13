import random
from math import sqrt

#General functions
#believe or not 100% original lol 

# def AssertFunction(condition: bool, errorFunction: Callable[[any], any] = rasieAssertionError, *params: any) -> any:
#     if not condition:
#         return errorFunction(params)
    
def Assert(condition: bool, errorMsg: str | None = None) -> None:
    """Assert the condition to be true, raises AssertionError otherwise.

    Parameters
    ----------
    condition : bool
        the condition to be checked
    errorMsg : str | None, optional
        the error message to be thrown, by default None

    Raises
    ------
    AssertionError
        if the condition is false
    """
    if not condition: 
        raise AssertionError(errorMsg)
    
def isOdd(n: int) -> bool: 
    Assert(n is int, "n should be an integer")
    return (bool)(n & 1)

def isEven(n: int) -> bool:
    return not isOdd(n)

def isPrime(n: int) -> bool:
    """Check whether n is a prime number

    Parameters
    ----------
    n : int

    Returns
    -------
    bool
    """
    Assert(n is int, "n should be an integer")
    if isEven(n): return False
    for i in range(3, int(sqrt(n))+1, 2):
        #print(f'i is {i}')
        if n % i == 0: 
            return False
    return True

def getInputs(number: int, _type: any = None, _eval = True) -> list:
    """Gets a given number of input
    i.e. a, b, c = getInput(3, int, False)

    Parameters
    ----------
    number : int
        the number of inputs to return
    _type : type, optional
        the type in which the inputs converts to, by default None
    _eval : bool, optional
        evals the inputs when _type is not presented, each input may convert to different types,
            by default True

    Returns
    -------
    list
        list of input to be destructured
    """
    
    l = []
    for _ in range(number):
        if not _type:
            if _eval:
                l.append(eval(input()))
            else: l.append(input)
        else:
            l.append(_type(input()))
            
    return l

def chance(percentage: float) -> bool:
    """Gets a boolean based on the given percentage

    Parameters
    ----------
    percentage : float
        the percentage for True happens

    Returns
    -------
    bool
    """
    if percentage >= 100: return True
    if percentage <= 0: return False
        
    return random.random() * 100 <= percentage
    

class Matrix:
    """Simple Matrix class"""
    def __init__(self, row: int, col: int, init: int | float = 0) -> None:

        self.row = row
        self.col = col
        self.mat = []
        for _ in range(row):
            _l = []
            for _ in range(col):
                _l.append(init)
            self.mat.append(_l)
    @staticmethod
    def fromList(_list: list):
        """Creates a Matrix from 2D list

        Parameters
        ----------
        _list : list
            the 2D list

        Returns
        -------
        Matrix
            A new Matrix
        """
        row = len(_list)
        col = len(_list[0])
        out = Matrix(row, col)
        out.mat = _list
        return out
    
    def toList(self) -> list:
        """Convert the current Matrix to a 2D list

        Returns
        -------
        list
            Casted list
        """
        return self.mat
    
    def __add__(self, other):
        if not type(other) == Matrix:
            return self.__addEach(other)

        if self.size() != other.size(): 
            return self.mat
        
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] + other[i][j])
            out.append(_l)
                                
        return Matrix.fromList(out)
    
    def __addEach(self, n: int | float):
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] + n)
            out.append(_l)
                                
        return Matrix.fromList(out)

                
    def __mul__(self, other):
        if not type(other) == Matrix:
            return self.__mulEach(other)
            
        if self.size()[1] != other.size()[0]: #or self.size()[1] != other.size()[0]:
            return "Error lol"
        
        out = []
        for i in range(self.row):
            _l = []
            for j in range(other.col):
                _sum = 0
                for x in range(self.col):
                    _sum += self[i][x] * other[x][j]
                print(_sum  )
                _l.append(_sum)
            out.append(_l)
               
        return Matrix.fromList(out)
        
        
    def __mulEach(self, n: int | float):
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] * n)
            out.append(_l)
                                
        return Matrix.fromList(out)
    
    def size(self) -> tuple:
        """Gets the size of the Matrix

        Returns
        -------
        tuple
            [0]: row
            [1]: col
        """
        return (self.row, self.col)

    def randomize(self, _min = 0, _max = 50) -> None:
        """Randomizes the Matrix elements

        Parameters
        ----------
        _min : int, optional
            default 0
        _max : int, optional
            default 50
        """
        from random import randint
        for i in range(self.row):
            for j in range(self.col):
                self[i][j] = randint(_min, _max)
    
    def transpose(self):
        """Gets the transposed Matrix

        Returns
        -------
        Matrix
            Transposed Matrix
        """
        mat = Matrix(self.col, self.row, 0)
        for i in range(self.row):
            for j in range(self.col):
                mat[j][i] = self.mat[i][j]
        return mat
                
    def __getitem__(self, key):
        return self.mat[key] 
    
    def __str__(self):
        res = []
        for i in range(self.row):
            j = str(self.mat[i])
            res.append(j)
        
        res = ', \n '.join(res)
        return f"[\n {res}\n]"