import UI.window as win
from Struct.Vector import Vector
from Struct.Matrix import Matrix
import tkinter as tk

class boardgrid:
    def __init__(self) -> None:
        pass

    def initialize(self, window: win.window) -> None:
        canvas = tk.Canvas(window.win, 
                           background=win.BackgroundColor,
                           highlightthickness=3, highlightbackground=win.BorderColor,
                           width=win.WinWidth, height=win.WinHeight)
        
        canvas.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.grid = Matrix(4, 4)
        self.initGrid(canvas)

        self.canvas = canvas

    def initGrid(self, canvas: tk.Canvas):
        size = Vector(win.WinWidth / 4, win.WinHeight / 4)
        for i in range(self.grid.row):
            for j in range(self.grid.col):
                r = canvas.create_rectangle(size.x * i + 3, size.y * j + 3,
                                            size.x * (i + 1) + 3, size.y * (j + 1) + 3,
                                            fill=win.BackgroundColor, outline=win.BorderColor,
                                            width=12)
                self.grid[i][j] = r

    def updateGrid(self, dir: Vector):
        
        pass