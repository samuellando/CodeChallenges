class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""

        for c in s:
            o = ord(c)
            if o >= 65 and o <= 90:
                r += c.lower()
            elif o >= 97 and o <= 122:
                r += c
            elif o >= 48 and o <= 57:
                r += c
        return r == r[::-1]
        
