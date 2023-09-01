class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        prev = 0
        p = 0 # Pointer
        for i, n in enumerate(nums):
            if n == prev and c < 2:
                if c == 2:
                    # Reome it
                    pass
                else:
                    c += 1
                    nums[p] = nums[i]
                    p += 1
            else:
                c = 1
                prev = n
                nums[p] = nums[i]
                p += 1
        
        return p
