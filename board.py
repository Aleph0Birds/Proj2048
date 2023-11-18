from Struct.Matrix import Matrix
from Struct.Vector import Vector
from UI.boardgrid import boardgrid
from typing import Literal

class Board:
    def __init__(self, boardgrid: boardgrid) -> None:
        ### Task 1 ###
        mat = Matrix(4, 4)
        ### Task 2 ###
        from random import choice
        from helper.utility import chance
        n = 0
        while n < 2:
            r, c = choice(range(4)), choice(range(4))
            if mat[r][c] != 0:
                continue
            
            mat[r][c] = bool(chance(50)) + 1
            n += 1
        boardgrid.updateBoard(mat)
        self.boardgrid = boardgrid
        self.mat = mat
        self.gravityDir = Vector.Zero


    def gravity(self, dir: Literal["Up", "Down", "Right", "Left"]) -> None:
        """Defy the law of gravity within the board, the bottom changes regarding to the gravity

        Parameters
        ----------
        dir : Literal[&quot;Up&quot;, &quot;Down&quot;, &quot;Right&quot;, &quot;Left&quot;]
            gravity direction
        """
        #  0 -1  0
        # -1  0  1
        #  0  1  0
        vertical = -1 if dir == "Up" else 1 if dir == "Down" else 0
        horizontal = -1 if dir == "Left" else 1 if dir == "Right" else 0
        self.gravityDir = Vector(horizontal, vertical)
        ### Task 4 ###
        self.update(horizontal, vertical)

    def update(self, signX: int, signY: int):
        # update ordered from bottom to top according to the gravity direction
        # bottom is exclusive since always at the grounded state
        #         0             1 Down            -1 Up
        iWay = [range(4), range(2, -1, -1), range(1, 4, 1)][signY]
        #         0             1 ->              -1 <-
        jWay = [range(4), range(2, -1, -1), range(1, 4, 1)][signX]

        for i in iWay:
            for j in jWay:
                #ignores empty tiles
                if self.mat[i][j] == 0: continue

                # move the tile according to the direction
                movedTo = self.moveY(i, j, signY) if signX == 0 else self.moveX(i, j, signX)

                ### move visual
                self.boardgrid.moveRect(i, j, movedTo)

        #self.boardgrid.updateBoard(self.mat)
        #print(self.mat)

    def moveX(self, i: int, j: int, signX: int) -> tuple:

        row = self.mat[i]
        jWay = range(j+1, 4, 1) if signX == 1 else range(j-1, -1, -1)
        for _j in jWay:
            #ignores empty tiles in between
            if row[_j] == 0: continue
            if row[_j] == row[j]:
                # merge
                row[j] = 0
                row[_j] += 1
            else:
                # stack
                temp = row[j]
                row[j] = 0
                row[_j - signX] = temp
            return i, _j
        
        # touches ground
        row[_j] = row[j]
        row[j] = 0 
        return i, _j

    def moveY(self, i: int, j: int, signY: int) -> tuple:
        #col = self.mat[j] nope can't do that

        iWay = range(i+1, 4, 1) if signY == 1 else range(i-1, -1, -1)
        for _i in iWay:
            #ignores empty tiles in between
            if self.mat[_i][j] == 0: continue
            if self.mat[_i][j] == self.mat[i][j]:
                # merge
                self.mat[i][j] = 0
                self.mat[_i][j] += 1
            else:
                # stack
                temp = self.mat[i][j]
                self.mat[i][j] = 0
                self.mat[_i - signY][j] = temp
            return _i, j
        
        # touches ground
        self.mat[_i][j] = self.mat[i][j]
        self.mat[i][j] = 0 
        return _i, j