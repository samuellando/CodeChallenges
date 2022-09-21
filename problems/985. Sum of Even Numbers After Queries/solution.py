class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        
        for n in nums:
            if n%2 == 0:
                s += n
        
        out = []
        for q in queries:
            # Remove the value from s if it is in there.
            if nums[q[1]] % 2 == 0:
                s -= nums[q[1]]
                
            nums[q[1]] = nums[q[1]] + q[0]
            
            # Add if back if it is still even
            if nums[q[1]] % 2 == 0:
                s += nums[q[1]]
            
            out.append(s)
        
        return out
