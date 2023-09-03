class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def dest(i):
            return (i + k) % len(nums)
        
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            res[dest(i)] = n
        
        for i, r in enumerate(res):
            nums[i] = r
