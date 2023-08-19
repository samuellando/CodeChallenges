class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        
        for row in dp:
            row[n-1] = 1
        
        dp[m-1] = [1] * n
        
        # Paths from position i, j is paths from position i + 1 + those from j + 1 
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]
