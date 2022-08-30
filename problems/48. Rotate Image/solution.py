class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        j = (n-1) - i
        i = j
        """
        n = len(matrix)
        for i in range((n - 1)//2 + 1):
            for j in range(i, n - 1 - i):
                ti = j
                tj = n - 1 - i
                t = matrix[i][j]
                
                while True:
                    t = t + matrix[ti][tj]
                    matrix[ti][tj] = t - matrix[ti][tj]
                    t = t - matrix[ti][tj]
                    
                    if ti == i and tj == j:
                        break
                    
                    tempi = ti
                    ti = tj
                    tj = n - 1 - tempi
        
