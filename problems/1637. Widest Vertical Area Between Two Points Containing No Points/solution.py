class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # We only care for the x coordinates
        xs = []
        for p in points:
            xs.append(p[0])

        xs.sort()

        ans = 0

        for i in range(1, len(xs)):
            if xs[i]  - xs[i-1] > ans:
                ans = xs[i] - xs[i-1]
        
        return ans

