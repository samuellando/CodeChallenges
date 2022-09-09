class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """"
        count = 0
        comp = 0
        for c in properties:
            for c2 in properties:
                comp += 2
                if c2[0] > c[0] and c2[1] > c[1]:
                    count += 1
                    break
        print(comp)
        
        return count
        """
        """
        p = properties
        at = {}
        
        for i in range(len(p)):
            if p[i][0] in at:
                at[p[i][0]].append(i)
            else:
                at[p[i][0]] = [i]
        
        
        count = 0
        for i in range(len(p)):
            brk = False
            for key in at:
                if key > p[i][0]:
                    for c in at[key]:
                        if p[c][1] > p[i][1]:
                            count += 1
                            brk = True
                            break
                    if brk:
                        break
                        
        return count
        """
        p = properties
        p.sort(key = lambda v : (v[0], v[1]))
        
        maxd = len(p) - 1
        maxdp = -1
        count = 0
        for i in reversed(range(len(p))):
            if p[i][1] > p[maxd][1]:
                # highest d, and not higher at, so cannot be eliminated.
                if p[i][0] < p[maxd][0]:
                    maxdp = maxd
                maxd = i
            
            elif (p[maxd][0] == p[i][0] and maxdp > 0 and p[maxdp][1] > p[i][1]) or (p[maxd][0] != p[i][0] and p[maxd][1] > p[i][1]):
                count += 1
            
        return count
