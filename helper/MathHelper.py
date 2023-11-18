from Struct.Vector import Vector


# interpolation
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
    if _min == _max: return _min
    if _min > _max:
        _min, _max = _max, _min
    return clamp(_min, _max, _min + t * (_max - _min))

def lerpVec(_min: Vector, _max: Vector, t: float) -> Vector:
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
    if _min == _max: return _min
    
    return clampVec(_min, _max, _min + t * (_max - _min))

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
    
def clampVec(lowerBound: Vector, upperBound: Vector, v: Vector) -> Vector:
    """Limits x into the range of 2 values

    Parameters
    ----------
    lowerBound : Vector
        minimum position
    upperBound : Vector
        maximum position
    v : Vector
        input vector v
    Returns
    -------
    Vector
        clamped Vector
    """
    x = lowerBound.x if v.x < lowerBound.x else upperBound.x if v.x > upperBound.x else v.x
    y = lowerBound.y if v.y < lowerBound.y else upperBound.y if v.y > upperBound.y else v.y
    return Vector(x, y)