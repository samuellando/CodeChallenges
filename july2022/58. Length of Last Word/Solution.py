class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        for t in s[::-1]:
            if len(t) > 0:
                return len(t)
        return 0
        
