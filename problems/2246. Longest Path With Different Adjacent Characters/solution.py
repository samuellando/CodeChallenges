class Solution:
    def longestPath(self, parent: List[int], chrs: str) -> int:
        children = [[] for i in range(len(parent))]
        lb = [1] * len(parent) # longest branch of subtree rooted at node i
        lp = 0 # longest path in general.

        for n, p in enumerate(parent):
            if p >= 0:
                children[p].append(n)

        s = [0]
        cb = [] # Callback in reverse order. 

        while len(s) > 0:
            n = s.pop()
            for c in children[n]:
                s.append(c)
            cb.append(n)
        
        """ 
        Cases:
            leaf => P & B is 1
            2 max children branches wo mathcing char + 1 compare to LP
            LB max child brnach wo mathcing char + 1 compare LP
        """

        while len(cb) > 0:
            n = cb.pop()
            lsbs = []
            for c in children[n]:
                if chrs[n] != chrs[c]:
                    if lb[c] + 1 > lb[n]:
                        lb[n] = lb[c] + 1
                    lsbs.append(lb[c])
            
            if lb[n] > lp:
                lp = lb[n]
            
            lsbs.sort(reverse=True)
            if len(lsbs) >= 2 and lsbs[0] + lsbs[1] + 1 > lp:
                lp = lsbs[0] + lsbs[1] + 1
            
        return lp
