class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        a = [0] * len(queries)

        for i, q in enumerate(queries):
            r = q
            for n in nums:
                if n <= r:
                    a[i] += 1
                    r -= n
        
        return a
