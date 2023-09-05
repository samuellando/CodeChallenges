class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        
        for c in candidates:
            if target - c > 0:
                rem = self.combinationSum(candidates, target - c)
                for r in rem:
                    acc.append(r + [c])
            elif target - c == 0:
                acc.append([c])
        
        i = 0
        while i < len(acc):
            l1 = acc[i]
            j = 0
            while j < len(acc):
                l2 = acc[j]
                if i == j:
                    j += 1
                    pass
                else:
                    l1.sort()
                    l2.sort()
                    match = True
                    for e1, e2 in zip(l1, l2):
                        if e1 != e2:
                            match = False
                            break
                    if match:
                        del acc[j]
                    else:
                        j += 1
            i += 1

        return acc
