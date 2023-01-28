class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m + 1)]

        ans = []
        for q in queries:
            i = P.index(q)
            p = P.pop(i)
            P.insert(0, p)
            ans.append(i)

        return ans

