class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        for i, n in enumerate(candidates):
            rem = candidates[:i] + candidates[i+1:]
            missing = target - n
            if i > 0 and n == candidates[i-1]:
                continue
            if missing == 0:
                res.append([n])
            elif missing > 0:
                req = self.combinationSum2(rem, missing)
                for r in req:
                    res.append(r + [n])
            else:
                break

        for r in res:
            r.sort()

        s =  set(tuple(i) for i in res)
        return list(list(i) for i in s)

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1], 27))
