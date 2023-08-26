class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for n in nums:
            counts[n] += 1
        
        for i, _ in enumerate(nums):
            if counts[0] > 0:
                counts[0] -= 1
                nums[i] = 0
            elif counts[1] > 0:
                counts[1] -= 1
                nums[i] = 1
            elif counts[2] > 0:
                counts[2] -= 1
                nums[i] = 2
