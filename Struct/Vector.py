from typing import overload

class Vector:

    def __init__(self, x: float | int, y: float | int | None = None):
        self.x = x 
        self.y = x if y is None else y
    
    def __str__(self):
        return f"Vec({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"V({self.x}, {self.y})"

Zero = Vector(0)
One = Vector(1)
Vector.Zero: Vector = Zero
Vector.One: Vector = One