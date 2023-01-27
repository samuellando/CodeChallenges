class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        # load the diagonals for sorting.
        d = []
        for j in range(-1*len(mat) + 1, len(mat[0])):
            i = 0
            l = []
            while i < len(mat) and j < len(mat[0]):
                if j >=0:
                    l.append(mat[i][j])
                i += 1
                j += 1
            d.append(l)
        
        # sort the diagonals
        for l in d:
            l.sort()
        
        # and reload them into mat
        for j in range(-1*len(mat) + 1, len(mat[0])):
            i = 0
            l = d.pop(0)
            while i < len(mat) and j < len(mat[0]):
                if j >=0:
                    mat[i][j] = l.pop(0)
                i += 1
                j += 1
        
        return mat
