class Node:
    def __init__(self):
        self.adj = []
        self.v = False

    def con(self, n2):
        if n2 != None:
            self.adj.append(n2)
            n2.adj.append(self)

class Solution:
    def dfs(self, n):
        n.v = True
        for n2 in n.adj:
            if not n2.v:
                self.dfs(n2)

    def numIslands(self, grid: List[List[str]]) -> int:
        nodes = []
        for r in grid:
            nr = []
            for e in r:
                if e == "1":
                    n = Node()
                else:
                    n = None
                nr.append(n)
            nodes.append(nr)

        for i in range(len(nodes)):
            for j in range(len(r)):
                n = nodes[i][j]
                if n != None:
                    if i < len(nodes)-1:
                        n.con(nodes[i+1][j])
                    if j < len(r)-1:
                        n.con(nodes[i][j+1])
                    if j < len(r)-1 and i < len(nodes)-1:
                        n.con(nodes[i][j+1])

        c = 0
        for i in range(len(nodes)):
            for j in range(len(r)):
                n = nodes[i][j]
                if n != None and not n.v:
                    c += 1
                    self.dfs(n)

        return c
