class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp [-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            # We can get to the end from position i if there is a True in it's range.
            for j in range(i+1, min(len(nums), i + nums[i] + 1)):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]
