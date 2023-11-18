
# interpolation
from typing import overload
from Struct.Vector import Vector


def lerp(_min: float, _max: float, t: float) -> float:
    """Linearly interpolates t from _min to _max 
        for t in interval [0, 1]

    Parameters
    ----------
    _min : float
        base value
    _max : float
        max value
    t : float
        from 0 to 1

    Returns
    -------
    float
        value between _min and _max
    """
    return _min + t * (_max - _min)

@overload
def lerp(_min: Vector, _max: Vector, t: float) -> Vector:
    """Linearly interpolates t from _min to _max 
        for t in interval [0, 1]

    Parameters
    ----------
    _min : float
        base value
    _max : float
        max value
    t : float
        from 0 to 1

    Returns
    -------
    float
        value between _min and _max
    """
    return _min + t * (_max - _min)

def unlerp(_min: float, _max: float, x: float) -> float:
    """Gets the ratio of x from _min to _max

    Parameters
    ----------
    _min : float
    _max : float
    x : float

    Returns
    -------
    float
        unlerped value, or t inputted for the lerp function
    """
    return (x - _min) / (_max - _min)

def clamp(lowerBound: int | float, upperBound: int | float, x: int | float) -> int | float:
    """Limits x into the range of 2 values

    Parameters
    ----------
    lowerBound : int | float
        minimum value
    upperBound : int | float
        maximum value
    x : int | float
        input value x
    Returns
    -------
    int | float
        clamped value
    """
    return lowerBound if x < lowerBound else upperBound if x > upperBound else x
    