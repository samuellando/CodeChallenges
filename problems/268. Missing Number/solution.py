class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p = [False] * (len(nums) + 1 )

        for n in nums:
            p[n] = True

        for i, v in enumerate(p):
            if not v:
                return i
                
