class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        l = [[0,0] for i  in range(n)]

        for t in trust:
            l[t[0]-1][0] += 1
            l[t[1]-1][1] += 1

        for i, t in enumerate(l): 
            if t[0] == 0 and t[1] == n-1:
                return i+1
        
        return -1
