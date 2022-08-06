class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        out = []

        for d in digits:
            t = []
            for l in m[int(d) - 2]:
                if len(out) == 0:
                    t.append(l)
                else:
                    for o in out:
                        t.append(o+l)
            out = t

        return out
