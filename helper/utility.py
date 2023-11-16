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