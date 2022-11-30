class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        
        for e in arr:
            if e in m:
                m[e] += 1
            else:
                m[e] = 1
        
        m2 = {}
        
        for e in m.values():
            if e in m2:
                return False
            else:
                m2[e] = 1
                
        return True
