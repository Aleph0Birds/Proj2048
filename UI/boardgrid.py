import UI.window as win
from Struct.Vector import Vector
from Struct.Matrix import Matrix
import tkinter as tk

padding = 36
borderWidth = 10
dw = borderWidth / 4
dp = padding / 2
size = Vector((win.WinWidth - padding) / 4)


class boardgrid:
    def __init__(self, window: win.window) -> None:
        canvas = tk.Canvas(window.win, 
                           background=win.BackgroundColor, borderwidth=0,
                           width=win.WinWidth, height=(size.y*4+padding*4))
        
        canvas.grid(row = 2, column=0, columnspan=4)
        self.grid = Matrix(4, 4)
        self.initGrid(canvas)

        self.canvas = canvas

    def initGrid(self, canvas: tk.Canvas):
        for i in range(self.grid.row):
            for j in range(self.grid.col):
                r = canvas.create_rectangle(size.x * i + dp,
                                            (size.y * j + dp),
                                            size.x * (i + 1) + dp,
                                            (size.y * (j + 1) + dp),
                                            fill=win.BoardColor, outline=win.BorderColor,
                                            width=borderWidth)
                self.grid[i][j] = r

    def updateGrid(self, dir: Vector):
        
        pass