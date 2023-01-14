class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        e = [] #  Equivilancy classes.
        l = {} # Lookups.

        for (a, b) in zip(s1, s2):
            if a == b:
                continue
            ca = -1
            cb = -1

            if a in l:
                ca = l[a]
            if b in l:
                cb = l[b]
            
            if ca >= 0 and ca == cb:
                continue
            
            if ca >= 0 and cb >= 0:
                for c in e[cb]:
                    l[c] = ca
                e[ca] = e[ca] + e[cb]
            elif ca >= 0:
                e[ca].append(b)
                l[b] = ca
            elif cb >= 0:
                e[cb].append(a)
                l[a] = cb
            else:
                e.append([a,b])
                l[a] = len(e) - 1
                l[b] = len(e) - 1

        for k in e:
            k.sort()
        ans = ""
        for c in baseStr:
            if c in l:
                ans += e[l[c]][0]
            else:
                ans += c
        
        return ans

