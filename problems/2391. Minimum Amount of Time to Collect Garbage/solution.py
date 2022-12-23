class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        t = 0

        m = {"P": 0, "G": 0, "M": 0}

        
        for i, h in enumerate(garbage):
            for c in "PGM":
                if c in h:
                    t += h.count(c)
                    m[c] = i
        
        for c in "PGM":
            for i in range(m[c]):
                print(c, m[c])
                t += travel[i]
        
        return t
