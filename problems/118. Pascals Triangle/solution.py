class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [[1]]

        for i in range(numRows -1):
            l = t[-1]
            n = [1]
            for j in range(len(l)-1):
                n.append(l[j] + l[j + 1])
            
            n.append(1)
            t.append(n)
        
        return t
        

