class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        l(i) = l(j) + 1 : arr[j] < nums[i]
        
        Follows the optimal substructure property.
        
        dp[i]
        """
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        
        m = 1
        for n in dp:
            if n > m:
                m = n
        
        return m
