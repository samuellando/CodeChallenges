from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        for i, c in enumerate(s):
            if c in d:
                v = d.get(c)
                v[1] += 1
            else:
                d[c] = [i, 1]
        
        for v in d.values():
            if v[1] == 1:
                return v[0]
        
        return -1 
