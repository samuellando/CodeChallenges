class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # If the rectangles are overlapping, there will be one point that is within th other.
        
        aA = (ax2 - ax1) * (ay2 - ay1)
        bA = (bx2 - bx1) * (by2 - by1)
        
        l = max(ax1, bx1)
        r = min(ax2, bx2)
        b = max(ay1, by1)
        t = min(ay2, by2)
        
        if r < l or t < b:
            oA = 0
        else:
            oA = (r - l) * (t - b)

        return aA + bA - oA
