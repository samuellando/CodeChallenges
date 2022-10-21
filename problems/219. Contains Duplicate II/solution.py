class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        
        for i, n in enumerate(nums):
            if n in m:
                for j in m[n]:
                    if abs(j - i) <= k:
                        return True  
                m[n].append(i)
            else:
                m[n] = [i]
        
        return False
