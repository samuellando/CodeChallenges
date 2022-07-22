class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
# A flower can be placed suronded by 2 zeros or a zero and an edge. Be greedy

        f = flowerbed
        m = 0
        for i in range(len(f)):
            if f[i] == 0 and (i-1 < 0 or f[i-1] == 0) and (i+1 == len(f) or f[i+1] ==0):
                f[i] = 1
                m = m + 1

        return m >= n
