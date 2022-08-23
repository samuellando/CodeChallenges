class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            t = self.permute(nums[:i]+nums[i+1:])
            for s in t:
                a.append([nums[i]] + s)
    
        return a

