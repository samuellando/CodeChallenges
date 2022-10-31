class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        
        for j in range(-1*n + 1, m):
            i = 0          
            v = -1
            while i < n and j < m:
                
                print(i, j)
                if j < 0:
                    pass
                elif v == -1:
                    v = matrix[i][j]
                elif matrix[i][j] != v:
                    return False
                
                i += 1
                j += 1
        
        return True
