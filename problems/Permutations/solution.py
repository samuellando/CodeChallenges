class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        ans = []
        
        for i, n in enumerate(nums):
            suf = self.permute(nums[:i]+nums[i+1:])
            for s in suf:
                ans.append([n] + s)
            
        return ans
