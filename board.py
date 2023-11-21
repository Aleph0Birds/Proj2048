from Struct.Matrix import Matrix
from Struct.Vector import Vector
from UI.boardgrid import boardgrid
from typing import Literal
from random import choice, randint
from helper.utility import chance

class Board:
    def __init__(self, boardgrid: boardgrid) -> None:
        ### Task 1 ###
        mat = Matrix(4, 4)
        self.mat = mat
        ### Task 2 ###
        
        self.max = 0
        self.generateNewTile()
        self.generateNewTile()
        
        for _ in range(randint(1, 3)):
            self.generateNewTile(-1)
        
        boardgrid.updateBoard(mat)
        self.boardgrid = boardgrid
        self.gravityDir = Vector.Zero
        self.score = 0
        self.bestScore = 0
        self.breakNum = randint(7, 9)


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

    def generateNewTile(self, type: int = 0) -> None:
        """Generates new tiles on the board

        Parameters
        ----------
        type : int, optional
            type of the tile, -1 represents obstacle, by default 0
        """
        if not self.haveSpace(): return
        
        while True:
            r, c = choice(range(4)), choice(range(4))
            if self.mat[r][c] != 0:
                continue
            
            self.mat[r][c] = n = bool(chance(50)) + 1 if type == 0 else -1
            self.max = n if n > self.max else self.max
            break

    def update(self, signX: int, signY: int):
        # update ordered from bottom to top according to the gravity direction
        # bottom is exclusive since always at the grounded state
        #         0             1 Down            -1 Up
        iWay = [range(4), range(2, -1, -1), range(1, 4, 1)][signY]
        #         0             1 ->              -1 <-
        jWay = [range(4), range(2, -1, -1), range(1, 4, 1)][signX]

        for i in iWay:
            for j in jWay:
                #ignores empty tiles and obstacles
                if self.mat[i][j] <= 0: continue

                # move the tile according to the direction
                movedTo = self.moveY(i, j, signY) if signX == 0 else self.moveX(i, j, signX)

                ### move visual
                self.boardgrid.moveRect(i, j, movedTo)

        _max = 0
        for i in range(4):
            _max2 = max(self.mat[i])
            if _max2 > _max:
                _max = _max2
        if _max > self.breakNum:
            # breaks the obstacle
            self.eradicateObstacle()

    def eradicateObstacle(self):
        for i in range(4):
            for j in range(4):
                if self.mat[i][j] == -1:
                    self.mat[i][j] = 0

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
                ### Task 7 ###
                self.score += 2 ** row[_j]
                return i, _j
            else:
                # stack
                temp = row[j]
                row[j] = 0
                row[_j - signX] = temp
                return i, _j - signX
        
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
                self.score += 2 ** self.mat[_i][j]
                return _i, j
            else:
                # stack
                temp = self.mat[i][j]
                self.mat[i][j] = 0
                self.mat[_i - signY][j] = temp
                return _i - signY, j
        
        # touches ground
        self.mat[_i][j] = self.mat[i][j]
        self.mat[i][j] = 0 
        return _i, j
    
    def haveSpace(self) -> bool:
        for i in range(4):
            if 0 in self.mat[i]: return True
        return False
    
    def isGameover(self) -> bool:
        if self.haveSpace():
            return False
        
        for i in range(4):
            for j in range(4):
                this = self.mat[i][j]
                if this == -1: continue
                neighbours = self.mat.getAdjacentValues(i, j)
                if this in neighbours:
                    return False
        
        return True
    
    def restartBoard(self):
        self.mat = Matrix(4, 4)
        self.max = 0
        self.generateNewTile()
        self.generateNewTile()
        for _ in range(randint(1, 3)):
            self.generateNewTile(-1)
        self.score = 0
        self.gravityDir = Vector.Zero