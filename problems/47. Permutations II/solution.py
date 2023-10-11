class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = Counter(map(lambda l: tuple(l), self.permute(nums)))
        return list(map(lambda t:list(t), res.keys()))
    
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        res = deque()
        for i, n in enumerate(nums):
            ss = self.permute(nums[:i] + nums[i+1:])
            for s in ss:
                res.append([n] + s)
        
        return list(res)
