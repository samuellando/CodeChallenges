class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i+k < len(nums) - 1:
            nums[i+1] = nums[i+k+1] 
            if nums[i] == nums[i+1]:
                k += 1
            else:
                i += 1
        
        return len(nums) - k
