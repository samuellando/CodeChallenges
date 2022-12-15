def abs(i):
    return i if i >= 0 else -1 * i

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        sol = nums[0] + nums[1] + nums[2]
        for i, n1 in enumerate(nums[:-1]):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(sol - target) > abs(s - target):
                    sol = s
                
                if s > target:
                    k -= 1
                else:
                    j += 1
        
        return sol
