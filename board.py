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
        """Defy the law of gravity within the board

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
        self.update()

    def update(self):
        for i in range(4):
            for j in range(4):
                if self.mat[i][j] == 0: continue
                # TODO implement visual changes
                moved = self.move(i, j)

        self.boardgrid.updateBoard(self.mat)
        print(self.mat)

    def moveX(self, i: int, j: int) -> tuple:
        pass

    def moveY(self, i: int, j: int) -> tuple:
        pass