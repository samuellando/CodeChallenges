class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i -= 2
        
            i += 1
            if i < 0:
                i = 0
        
        return s
