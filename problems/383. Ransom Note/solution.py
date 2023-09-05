class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for l in magazine:
            if l in m:
                m[l] += 1
            else:
                m[l] = 1
        
        for l in ransomNote:
            if l in m and m[l] > 0:
                m[l] -= 1
            else:
                return False
        
        return True
