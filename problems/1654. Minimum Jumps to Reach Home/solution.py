class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dp = {}

        for n in forbidden:
            dp[n] = (-1, 1)
        
        q = [(0, 0)]

        dp[0] = (0, 0)
        dist = 0
        while len(q) > 0:
            l = len(q)
            for _ in range(l):
                p, back = q.pop(0)

                if p == x:
                    return dist
                
                if p+a < 2000 + a + b and (dp.get(p+a) is None or (dp[p+a][0] != -1 and dp[p+a][1] == 1)):
                    dp[p+a] = (dist + 1, 0)
                    q.append((p+a, 0))
                if p - b >= 0 and dp.get(p-b) is None and back != 1:
                    dp[p-b] = (dist + 1, 1)
                    q.append((p-b, 1))
                
            dist += 1
        
        return -1
