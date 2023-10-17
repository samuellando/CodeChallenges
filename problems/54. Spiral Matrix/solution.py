class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        minR = 1
        maxR = n-1
        minC = 0
        maxC = m-1

        res = [] 
        i = 0
        j = 0

        if len(matrix[0]) > 1:
            dr = 0
            dc = 1
        else:
            dr = 1
            dc = 0

        while len(res) < n*m:
            res.append(matrix[i][j])
            if dc > 0:
                j += 1
                if j == maxC:
                    dc = 0
                    dr = 1
                    maxC -= 1
            elif dr > 0:
                i += 1
                if i == maxR:
                    dc = -1
                    dr = 0
                    maxR -= 1
            elif dc < 0:
                j -= 1
                if j == minC:
                    dc = 0 
                    dr = -1
                    minC += 1
            elif dr < 0:
                i -= 1
                if i == minR:
                    dc = 1
                    dr = 0
                    minR += 1

        return res

