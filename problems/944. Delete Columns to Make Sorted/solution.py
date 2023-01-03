class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1:
            return 0

        # Convert each string to a list.
        a = [list(s) for s in strs]

        # Transpose the 2d array.
        at = [list(x) for x in zip(*a)]

        count = 0
        for c in at:
            if not all(c[i+1] >= c[i] for i in range(len(c) - 1)):
                count += 1
        
        return count
