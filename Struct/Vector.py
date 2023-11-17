class Vector:
    def __init__(self, x: float | int, y: float | int = None):
        self.x = x 
        self.y = x if y is None else y

Vector.Zero: Vector = Vector(0)
Vector.One: Vector = Vector(1)