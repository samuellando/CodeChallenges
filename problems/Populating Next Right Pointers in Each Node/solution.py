"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Use a bfs, to list level by level
        if root == None:
            return None
        
        q = [root]
        
        while len(q) > 0:
            n = len(q)
            
            for i in range(n):
                p = q.pop(0)
                if i < n - 1:
                    p.next = q[0]
                
                if p.right != None:
                    q.append(p.left)
                    q.append(p.right)

                
        
        return root
