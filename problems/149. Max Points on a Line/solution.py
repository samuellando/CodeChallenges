class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        import math
        ans = 1


        # O(n^3)
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                onLine = 0
                vertical = p2[0] == p1[0]

                if not vertical:
                    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    b = p2[1] - m * p2[0]
                


                for p3 in points:
                    if not vertical and math.isclose(p3[1], m * p3[0] + b):
                        onLine += 1
                    elif vertical and p1[0] == p3[0]:
                        onLine += 1
                        
                if onLine > ans:
                    ans = onLine
        
        return ans

