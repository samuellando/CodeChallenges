class Node:
    def __init__(self, val):
        self.adj = []
        self.v = False
        self.val = val

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        nodes = [Node(i) for i in range(n)]

        for e in edges:
            nodes[e[0]].adj.append(nodes[e[1]])
            nodes[e[1]].adj.append(nodes[e[0]])
        
        return dfs(nodes[source], nodes[destination])

def dfs(s, d):
    if s == d:
        return True
    
    stk = [s]

    while len(stk) > 0:
        p = stk.pop(0)

        for n in p.adj:
            if n == d:
                return True
            if not n.v:
                stk.insert(0, n)
                n.v = True
    
    return False
            

