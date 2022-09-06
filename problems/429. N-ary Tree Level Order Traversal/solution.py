"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        m = {}
        s = []
        
        if root != None:
            s.append((root, 0))
            
        while len(s) != 0:
            p, d = s.pop(0)
            if not d in m.keys():
                m[d] = [p.val]
            else:
                m[d].append(p.val)
            
            for c in p.children:
                s.append((c, d+1))
        
        r = []
        for k in m:
            r.append(m[k])
            
        return r
        
