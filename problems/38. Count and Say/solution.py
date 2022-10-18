class Solution:
    def r(self, n):
        if n == 1:
            return "1"
        
        s = self.r(n-1)
        
        o = ""
        i = 0
        while i < len(s):
            c = 1
            j = i+1
            while j < len(s) and s[i] == s[j]:
                c += 1
                j += 1
            
            o += str(c) + s[i]
            i = j
        return o
    
    def countAndSay(self, n: int) -> str:
        return self.r(n)
        
