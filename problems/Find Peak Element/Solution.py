class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while r >= l:
            if r == l:
                return r
            mid = (r + l) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid+1] < nums[mid]):
                return mid
            elif mid != 0 and nums[mid-1] > nums[mid]:
                r = mid - 1
            elif mid != len(nums) - 1 and nums[mid+1] > nums[mid]:
                l = mid + 1
            else:
                return -1
        
        return -1
                
