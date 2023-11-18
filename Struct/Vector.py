from typing import overload
from math import sqrt

class Vector:

    def __init__(self, x: float | int, y: float | int | None = None):
        self.x = x 
        self.y = x if y is None else y

    def length(self) -> float:
        """Gets the length of the vector

        Returns
        -------
        float
        """
        return sqrt(self.x**2 + self.y**2)
    
    def normalize(self) -> None:
        """Resizes the vector to which with length 1"""
        mag = self.length()
        self.x /= mag
        self.y /= mag

    def normalized(self) -> None:
        """Gets the unit vector"""
        vec = self.copy()
        vec.normalize()
        return vec
    
    def __eq__(self, other) -> bool:
        if type(other) != Vector: 
            raise TypeError(f"other should be Vector, not {type(other)}")
        
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Vector(self.x, self.y)

    def __len__(self) -> float:
        return self.length()
    
    def __str__(self):
        return f"Vec({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"V({self.x}, {self.y})"
    
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __mul__(self, other):
        if type(other) not in [int, float]: 
            raise TypeError(f"other should be int or float, not {type(other)}")
        
        return Vector(self.x * other, self.y * other)
    __rmul__ = __mul__

    def __div__(self, other):
        if type(other) not in [int, float]: 
            raise TypeError(f"other should be int or float, not {type(other)}")
        
        return Vector(self.x / other, self.y / other)
    
    __rdiv__ = __div__
    __truediv__ = __div__

    def __add__(self, other):
        if type(other) != Vector: 
            raise TypeError(f"other should be Vector, not {type(other)}")
        
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        if type(other) != Vector: 
            raise TypeError(f"other should be Vector, not {type(other)}")
        
        return Vector(self.x - other.x, self.y - other.y)

Zero = Vector(0)
One = Vector(1)
Vector.Zero: Vector = Zero
Vector.One: Vector = One