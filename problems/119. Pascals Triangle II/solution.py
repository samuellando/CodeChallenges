class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [0] * (rowIndex + 1)
        r[0] = 1

        c = 0
        for i in range(rowIndex):
            for j in range(rowIndex , 0, -1):
                r[j] = r[j] + r[j-1]
        
        return r

