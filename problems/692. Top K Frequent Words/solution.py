class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        
        for w in words:
            if w in counts:
                counts[w] += 1
            else:
                counts[w] = 1
        
        g = {}
        for c in counts:
            if counts[c] in g:
                g[counts[c]].append(c)
            else:
                g[counts[c]] = [c]
            
        ks = list(g.keys())
        ks.sort(reverse=True)
        r = []
        for key in ks:
            g[key].sort()
            for w in g[key]:
                r.append(w)

        return r[:k]
