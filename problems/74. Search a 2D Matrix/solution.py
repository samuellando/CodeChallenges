class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        
        
        i = 0
        j = 0
        
        while m > 1:
            if matrix[i + m//2][0] > target:
                m = m - m // 2
            elif matrix[i + m//2][0] < target:
                i = i + m // 2
                m = m - m // 2
            else:
                return True
            
        while n > 1:
            if matrix[i][j + n // 2] > target:
                n = n - n // 2
            elif matrix[i][j + n // 2] < target:
                j = j + n // 2
                n = n - n // 2
            else:
                return True
            
        if n == 1 and m == 1:
            return target == matrix[0][0]
        
        return False
