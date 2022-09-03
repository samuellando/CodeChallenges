class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        if j < len(s):
            return False
        else:
            return True
