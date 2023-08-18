class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setToZero = {}
        
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if n == 0:
                    for i2 in range(len(matrix)):
                        if matrix[i2][j] != 0:
                            matrix[i2][j] = setToZero
                    for j2 in range(len(row)):
                        if matrix[i][j2] != 0:
                            matrix[i][j2] = setToZero
        
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if n == setToZero:
                    matrix[i][j] = 0
