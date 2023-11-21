
class Matrix:
    """Simple Matrix class"""
    def __init__(self, row: int, col: int, init: int | float = 0) -> None:

        self.row = row
        self.col = col
        self.mat = []
        for _ in range(row):
            _l = []
            for _ in range(col):
                _l.append(init)
            self.mat.append(_l)
    @staticmethod
    def fromList(_list: list):
        """Creates a Matrix from 2D list

        Parameters
        ----------
        _list : list
            the 2D list

        Returns
        -------
        Matrix
            A new Matrix
        """
        row = len(_list)
        col = len(_list[0])
        out = Matrix(row, col)
        out.mat = _list
        return out
    
    @staticmethod
    def createIdentity(n: int):
        """Creates an n by n identity matrix
        Parameters
        ----------
        n : int
            no. of row and column

        Returns
        -------
        Matrix
            an nxn identity matrix
        """
        mat = Matrix(n)
        for i in range(n):
            mat[i] = 1
        return mat

    @staticmethod
    def createZero(n: int):
        """Creates an n by n zero matrix

        Parameters
        ----------
        n : int
            no. of row and column

        Returns
        -------
        Matrix
            an nxn zero matrix
        """
        mat = Matrix(n)
        for i in range(n):
            mat[i] = 0
        return mat
    
    def toList2D(self) -> list[list]:
        """Convert the current Matrix to a 2D list

        Returns
        -------
        list
            Casted list
        """
        return self.mat
    
    def __add__(self, other):
        if type(other) in [int, float]:
            return self.__addEach(other)
        
        if type(other) != Matrix: 
            raise TypeError(f"Cannot perform addition between Matrix and {type(other)}")

        if self.size() != other.size(): 
            raise ValueError(f"Cannot add matrices with different size.")
        
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] + other[i][j])
            out.append(_l)
                                
        return Matrix.fromList(out)
    
    def __addEach(self, n: int | float):
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] + n)
            out.append(_l)
                                
        return Matrix.fromList(out)

                
    def __mul__(self, other):
        if type(other) in [int, float]:
            return self.__mulEach(other)
        
        if type(other) != Matrix: 
            raise TypeError(f"Cannot perform addition between Matrix and {type(other)}")
        
        if self.size()[1] != other.size()[0]: #or self.size()[1] != other.size()[0]:
            raise ValueError(f"Cannot multiply Matrix with {self.col} columns to Matrix with {other.row} rows.")
        
        out = []
        for i in range(self.row):
            _l = []
            for j in range(other.col):
                _sum = 0
                for x in range(self.col):
                    _sum += self[i][x] * other[x][j]
                print(_sum  )
                _l.append(_sum)
            out.append(_l)
               
        return Matrix.fromList(out)
        
        
    def __mulEach(self, n: int | float):
        out = []
        for i in range(self.row):
            _l = []
            for j in range(self.col):
                _l.append(self[i][j] * n)
            out.append(_l)
                                
        return Matrix.fromList(out)
    
    def size(self) -> tuple:
        """Gets the size of the Matrix

        Returns
        -------
        tuple
            [0]: row
            [1]: col
        """
        return (self.row, self.col)

    def randomize(self, _min = 0, _max = 50) -> None:
        """Randomizes the Matrix elements

        Parameters
        ----------
        _min : int, optional
            default 0
        _max : int, optional
            default 50
        """
        from random import randint
        for i in range(self.row):
            for j in range(self.col):
                self[i][j] = randint(_min, _max)
    
    def transpose(self):
        """Gets the transposed Matrix

        Returns
        -------
        Matrix
            Transposed Matrix
        """
        mat = Matrix(self.col, self.row, 0)
        for i in range(self.row):
            for j in range(self.col):
                mat[j][i] = self.mat[i][j]
        return mat
    
    def getAdjacentValues(self, i: int, j: int) -> list:
        l = []
        temp = i + 1
        compare = self.row
        for x in range(2):
            # skips out of bound index
            if temp < 0 or temp >= compare: continue
            l.append(self.mat[temp][j])
            temp = i - 1       
        temp = j + 1
        compare = self.col
        for x in range(2):
            # skips out of bound index
            if temp < 0 or temp >= compare: continue
            l.append(self.mat[i][temp])
            temp = j - 1
        return l
        
                
    def __getitem__(self, key) -> list:
        return self.mat[key] 
    
    def __str__(self):
        res = []
        for i in range(self.row):
            j = str(self.mat[i])
            res.append(j)
        
        res = ', \n '.join(res)
        return f"[\n {res}\n]"

Matrix.Identity2x2 = Matrix(2, 2)
