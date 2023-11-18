from typing import overload

class Vector:

    def __init__(self, x: float | int, y: float | int | None = None):
        self.x = x 
        self.y = x if y is None else y
    
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

    def __add__(self, other):
        if type(other) != Vector: 
            raise TypeError(f"other should be Vector, not {type(other)}")
        
        return Vector(self.x + other.x, self.y + other.y)
    

Zero = Vector(0)
One = Vector(1)
Vector.Zero: Vector = Zero
Vector.One: Vector = One