class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineStart(n, k, 1)

    def combineStart(self, n, k, start):
        if n - start +1 < k:
            return []
        if start == n:
            return [[start]]

        if k > 1:
            l = []
            for i in range(start, n):
                l = l + list(map(lambda x : [i] + x, self.combineStart(n, k - 1, i+1)))
            return l
        else:  # k == 1
            return [[i] for i in range(start,n+1)]

