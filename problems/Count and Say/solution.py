class Solution:
    def countAndSay(self, n: int) -> str:
        
        r = "1"
        
        while n > 1:
            s = r
            
            r = ""
            l = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    l += 1
                else:
                    r += str(l) + str(s[i-1])
                    l = 1
            
            r += str(l) + str(s[-1])
            n -= 1
        
        return r
                
