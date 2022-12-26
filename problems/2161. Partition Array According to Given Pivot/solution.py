class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        g = []
        p = []
        l = []

        for n in nums:
            if n > pivot:
                g.append(n)
            elif n < pivot: 
                l.append(n)
            else:
                p.append(n)
        
        return l + p + g
