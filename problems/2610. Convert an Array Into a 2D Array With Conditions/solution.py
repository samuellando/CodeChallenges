class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = {}

        mx = 0
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            if m[n] > mx:
                mx = m[n]

        ans = [[] for i in range(mx)]

        for i in range(mx):
            for k in m:
                if m[k] > i:
                    ans[i].append(k)
        
        return ans
