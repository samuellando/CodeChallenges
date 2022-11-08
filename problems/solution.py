class Solution:
    def makeGood(self, s: str) -> str:
        o = ""
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i+2:]
                if i != 0:  
                    i -= 2
                else:
                    i -= 1
            i += 1
        return s
                
