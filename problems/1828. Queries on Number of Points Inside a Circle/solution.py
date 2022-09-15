class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            (x, y) = (q[0], q[1])
            r = q[2]
            a = 0
            for p in points:
                (xp, yp) = (p[0], p[1])
                if r ** 2 >= (xp - x) ** 2 + (yp - y) ** 2:
                    a += 1
            ans.append(a)
            
        return ans
