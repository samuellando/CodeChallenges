class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        
        best = ""
        dp = [[] for i in range(len(s)+1)]
        
        l = 0
        
        while l <= len(s):
            for i in range(0, len(s) - l + 1):
                if l < 2:
                    dp[l].append(True)
                    best = s[i:i+l]
                elif s[i] == s[i+l-1] and dp[l-2][i+1]:
                    if len(best) < len(s[i:i+l]):
                        best = s[i:i+l]
                    dp[l].append(True)
                else:
                    dp[l].append(False)
            l = l + 1
        return best
    
