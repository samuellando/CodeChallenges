class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}

        for i, n in enumerate(groupSizes):
            if n in d:
                if len(d[n][-1]) < n:
                    d[n][-1].append(i)
                else:
                    d[n].append([i])
            else:
                d[n] = [[i]]
        
        o = []

        for n in d.values():
            for l in n:
                o.append(l)
            
        return o

        
