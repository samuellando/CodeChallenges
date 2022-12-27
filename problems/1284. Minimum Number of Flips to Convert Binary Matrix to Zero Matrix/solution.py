def flip(mat, i, j):
    if i > 0:
        if mat[i-1][j] == 1:
            mat[i-1][j]= 0
        else:
             mat[i-1][j] = 1

    if i < len(mat) - 1:
        if mat[i+1][j] == 1:
            mat[i+1][j] = 0
        else:
             mat[i+1][j] = 1
    
    if j > 0:
        if mat[i][j-1] == 1:
            mat[i][j-1]= 0
        else:
             mat[i][j-1] = 1

    if j < len(mat[0]) - 1:
        if mat[i][j+1] == 1:
            mat[i][j+1]= 0
        else:
             mat[i][j+1] = 1

    if mat[i][j] == 1:
        mat[i][j] = 0
    else:
        mat[i][j] = 1
    

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        ans = -1

        for n in range(0, 2 ** (len(mat) * len(mat[0]))):
            s = format(n, "{}b".format(len(mat) * len(mat[0])))[::-1]
            c = 0

            m = [[0] * len(mat[0]) for i in range(len(mat))] 
            for i, r in enumerate(mat):
                for j, e in enumerate(r):
                    if e == 1:
                        m[i][j] = 1
            
            for i, _ in enumerate(m):
                for j, _ in enumerate(r):
                    if s[i * len(m[0]) + j] == "1":
                        c += 1
                        flip(m, i, j)
            
            found = True
            for i, r in enumerate(m):
                for j, e in enumerate(r):
                    if e == 1:
                        found = False
                        
            if found:
                if c < ans or ans == -1:
                    ans = c
    
        return ans
            
    

