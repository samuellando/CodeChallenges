class Heap:
    def __init__(self, s):
        self.data = [None] * s
        self.last = 0
    
    def insert(self, n):
        self.data[self.last] = n
        i = self.last
        self.last += 1
        
        while i > 0 and self.data[i] > self.data[(i-1)//2]:
            self.data[i] = self.data[(i-1)//2]
            i = (i-1)//2
            self.data[i] = n
    
    def pop(self):
        res = self.data[0]
        i = 0
        while self.data[i] != None:
            l = 2*i + 1
            r = 2*i + 2
            if r < len(self.data) and self.data[r] is not None and self.data[l] is not None:
                if self.data[r] > self.data[l]:
                    self.data[i] = self.data[r]
                    i = r
                else:
                    self.data[i] = self.data[l]
                    i = l
            elif r < len(self.data) and self.data[r] is not None:
                self.data[i] = self.data[r]
                i = r
            elif l < len(self.data) and self.data[l] is not None:
                self.data[i] = self.data[l]
                i = l
            else:
                self.data[i] = None
        return res
                

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = Heap(len(nums))
        
        for n in nums:
            h.insert(n)
        
        res = None
        for _ in range(k):
            res = h.pop()
        
        return res
