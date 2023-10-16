# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        m = 1

        # Bad version is between m and n.

        while m != n:
            i = (m + n) // 2 # The  midpoint

            if isBadVersion(i):
                # It's <= i
                n = i
            else:
                # It's > i
                m = i+1
        
        return n
