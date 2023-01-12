class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = [False] * n
        adj = [[] for i in range(n)]
        counts = [{} for i in range(n)]
        matches = [0] * n

        q = [0]
        s = [0]

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        while len(s) < n:
            p = q.pop(0)
            visited[p] = True
            for a in adj[p]:
                if not visited[a]:
                    s.append(a)
                    q.append(a)
            

        while len(s) > 0:
            p = s[-1]
            counts[p][labels[p]] = 1

            for a in adj[p]:
                for k in counts[a]:
                    if k in counts[p]:
                        counts[p][k] += counts[a][k]
                    else:
                        counts[p][k] = counts[a][k]
            matches[p] = counts[p][labels[p]]
            s.pop()
        
        return matches
         
