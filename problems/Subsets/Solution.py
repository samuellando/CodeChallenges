class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        less = self.subsets(nums[:-1])
        
        for i in range(len(less)):
            less.append([nums[-1]] + less[i])
        
        return less
