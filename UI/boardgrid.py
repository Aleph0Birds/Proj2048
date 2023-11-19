import UI.window as win
from UI.Color2048 import Color
from Struct.Vector import Vector
from Struct.Matrix import Matrix
from helper.MathHelper import lerpVec
import tkinter as tk
import tkinter.font as tkf
import asyncio as aio

padding = 36
borderWidth = 10
dw = borderWidth / 4
dp = padding / 2
size = Vector((win.WinWidth - padding) / 4)
halfSize = size / 2

MOVE_SPEED = 6000 # 100 for debugging positon
'''The interval of animation, in screenUnit per seconds'''
ANIMATION_TICKRATE = 240 # seem like it affects the movement speed
DELTA_TIME = 1 / ANIMATION_TICKRATE


class boardgrid:
    def __init__(self, window: win.window) -> None:
        canvas = tk.Canvas(window.win, 
                           background=win.BackgroundColor, borderwidth=0,
                           width=win.WinWidth, height=(size.y*4+padding*4))
        
        canvas.grid(row = 2, column=0, columnspan=4)
        self.grid = Matrix(4, 4)
        self.initGridLayout(canvas)

        self.tasks = []
        self.window = window
        self.canvas = canvas
        self.font = tkf.Font(canvas, size=30, family="Segoe UI Semibold")

    def initGridLayout(self, canvas: tk.Canvas):
        for i in range(self.grid.row):
            for j in range(self.grid.col):
                _ = self.__createRect(canvas, i, j, win.BoardColor, win.BorderColor, borderWidth)

    def updateBoard(self, board: Matrix):
        for i in range(board.row):
            for j in range(board.col):
                    if self.grid[j][i] != 0:
                        self.canvas.delete(*self.grid[j][i])

        for i in range(board.row):
            for j in range(board.col):
                num = board[j][i]
                if num != 0:
                    color = Color.getColor(num)
                    fcolor = "white" if num > 2 else "#7a6e66"
                    self.grid[j][i] = (self.__createRect(self.canvas, i, j, color, win.BorderColor, borderWidth),
                                        self.__createFont(self.canvas, i, j, str(pow(2, num)), fcolor))


    async def waitAnimation(self, board: Matrix):
        await aio.gather(*self.tasks)
        self.tasks.clear()
        self.updateBoard(board)

    def moveRect(self, x: int, y: int, movedTo: tuple[int, int]):
        # rect
        rect, text = self.grid[x][y]
        curPos = self.__getPosition(x, y)
        toPos = self.__getPosition(*movedTo)
        _time = (curPos - toPos).length() / MOVE_SPEED

        # text
        tcurPos = curPos + halfSize + Vector(dw * 2)
        ttoPos = toPos + halfSize + Vector(dw * 2)

        #async moving
        self.tasks.append(self.updateFontPos(text, tcurPos, ttoPos, DELTA_TIME, 0, _time))
        self.tasks.append(self.updateRectPos(rect, curPos, toPos, DELTA_TIME, 0, _time))
        

    async def updateRectPos(self, id: int, fromPos: Vector, toPos: Vector,
                            dtime: float, curTime: float, totalTime: float):
        while curTime < totalTime:
        
            if fromPos.x > toPos.x or fromPos.y > toPos.y:
                curCoord = lerpVec(toPos, fromPos, 1 - curTime / totalTime)
            else:
                curCoord = lerpVec(fromPos, toPos, curTime / totalTime)
            
            self.canvas.moveto(id, *curCoord)
            self.canvas.update_idletasks()

            await aio.sleep(dtime)
            curTime += dtime

    async def updateFontPos(self, id: int, fromPos: Vector, toPos: Vector,
                            dtime: float, curTime: float, totalTime: float):
        while curTime < totalTime:
        
            if fromPos.x > toPos.x or fromPos.y > toPos.y:
                curCoord = lerpVec(toPos, fromPos, 1 - curTime / totalTime)
            else:
                curCoord = lerpVec(fromPos, toPos, curTime / totalTime)
            
            self.canvas.coords(id, *curCoord)
            self.canvas.update_idletasks()

            await aio.sleep(dtime)
            curTime += dtime


    def __createRect(self, canvas: tk.Canvas, i: int, j: int, bgcolor: str, borderColor: str = "", bWidth: int = 0) -> int:
        return canvas.create_rectangle(size.x * i + dp,
                                        (size.y * j + dp),
                                        size.x * (i + 1) + dp,
                                        (size.y * (j + 1) + dp),
                                        fill=bgcolor, outline=borderColor,
                                        width=bWidth)
    def __createFont(self, canvas: tk.Canvas, i: int, j: int, text: str, fgcolor: str) -> int:
        return canvas.create_text(size.x * (i + .5) + dp,
                                    (size.y * (j + .5) + dp),
                                    font=self.font,
                                    text=text,
                                    fill=fgcolor,
                                    anchor="center")
    def __getPosition(self, i: int, j: int) -> Vector:
        """gets the position of the tile by the grid indices

        Parameters
        ----------
        i : int
            index of row
        j : int
            index of column

        Returns
        -------
        Vector
            Position of the indexed tile
        """
        x = size.x * i + dp - dw * 2
        y = size.y * j + dp - dw * 2

        return Vector(y, x)