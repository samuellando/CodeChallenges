class Solution:
    def searchRange(self, nums: List[int], target: int, l=None, r=None) -> List[int]:
        res = [-1, -1]
        
        r = r if r is not None else len(nums) - 1
        l = l if l is not None else 0
        
        while r >= l:
            mid = (r + l) // 2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                lres = self.searchRange(nums, target, l, mid - 1)
                rres = self.searchRange(nums, target, mid + 1, r)
                res = [mid, mid]
                if lres[0] >= 0 and lres[0] < res[0]:
                    res[0] = lres[0]
                if rres[1] > res[1]:
                    res[1] = rres[1]
                return res
        return res
