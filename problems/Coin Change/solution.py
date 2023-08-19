class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        
        dp[0] = 0
        
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            else:
                p = []
                for c in coins:
                    j = i - c
                    k = i - j
                    if j < 0 or k < 0 or dp[j] == -1 or dp[k] == -1:
                        continue
                    else:
                        p.append(dp[j] + dp[k])
                if len(p) == 0:
                    dp[i] = -1
                else:
                    dp[i] = min(p)
        
        return dp[amount]
                    
            
# O(amount * coins)
