from typing import overload

class Vector:
    @overload
    def __new__(self, x: float | int, y: float | int):
        ...

    @overload
    def __new__(self, value: float | int):
        ...

    def __new__(self, x: float | int, y: float | int | None = None):
        self.x = x 
        self.y = x if y is None else y
        return self

Vector.Zero: Vector = Vector(0, 0)
Vector.One: Vector = Vector(1, 1)