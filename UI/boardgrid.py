import UI.window as win
from UI.Color2048 import Color
from Struct.Vector import Vector
from Struct.Matrix import Matrix
import tkinter as tk
import tkinter.font as tkf

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
        self.initGridLayout(canvas)

        self.canvas = canvas
        self.font = tkf.Font(canvas, size=30, family="Segoe UI Semibold")

    def initGridLayout(self, canvas: tk.Canvas):
        for i in range(self.grid.row):
            for j in range(self.grid.col):
                _ = self.__createRect(canvas, i, j, win.BoardColor)

    def updateGrid(self, dir: Vector):
        
        pass

    def updateBoard(self, board: Matrix):
        for i in range(board.row):
            for j in range(board.col):
                num = board[i][j]
                if num != 0:
                    color = Color.getColor(num)
                    fcolor = "white" if num > 2 else "#7a6e66"
                    self.grid[i][j] = (self.__createRect(self.canvas, i, j, color),
                                        self.__createFont(self.canvas, i, j, str(pow(2, num)), fcolor))

    def __createRect(self, canvas: tk.Canvas, i: int, j: int, bgcolor: str) -> int:
        return canvas.create_rectangle(size.x * i + dp,
                                        (size.y * j + dp),
                                        size.x * (i + 1) + dp,
                                        (size.y * (j + 1) + dp),
                                        fill=bgcolor, outline=win.BorderColor,
                                        width=borderWidth)
    def __createFont(self, canvas: tk.Canvas, i: int, j: int, text: str, fgcolor: str) -> int:
        return canvas.create_text(size.x * (i + .5) + dp,
                                    (size.y * (j + .5) + dp),
                                    font=self.font,
                                    text=text,
                                    fill=fgcolor)
