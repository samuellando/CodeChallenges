class Solution:
    def search(self, nums: List[int], target: int, l = None, r = None) -> int:
        l = l if l is not None else 0
        r = r if r is not None else len(nums) - 1
        
        while r >= l:
            mid = (r + l) // 2
            
            if nums[mid] == target:
                return mid
            elif (nums[r] >= nums[mid] and nums[l] >= nums[mid]) or (nums[r] <= nums[mid] and nums[l] <= nums[mid]):
                # It can be on either side:
                ls = self.search(nums, target, l, mid - 1) 
                rs = self.search(nums, target, mid+1, r)
                if max(ls, rs) >=0:
                    return max(ls, rs)
                else:
                    break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
