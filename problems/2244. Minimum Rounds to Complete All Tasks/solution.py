class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Start by taking a count of each difficulty level

        m = {}

        for t in tasks:
            if t in m:
                m[t] += 1
            else:
                m[t] = 1
        
        rounds = 0
        for d in m:
            v = m[d]
            while v > 0:
                if v == 1:
                    return -1
                elif v >= 3 and v - 3 != 1:
                    v -= 3
                else:
                    v -= 2
                rounds += 1
        
        return rounds
