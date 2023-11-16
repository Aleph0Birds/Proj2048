class Vector:
    def __init__(self, x: float | int, y: float | int = None):
        self.x = x 
        self.y = y if y is None else x

Vector.Zero: Vector = Vector(0)
Vector.One: Vector = Vector(1)