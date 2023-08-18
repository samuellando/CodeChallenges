class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        for i, c in enumerate(s):
            m = {c: True}
            l = 1
            for c2 in s[i+1:]:
                if not m.get(c2, False):
                    l += 1
                    m[c2] = True
                else:
                    break
            
            if l > res:
                res = l
            
        return res
