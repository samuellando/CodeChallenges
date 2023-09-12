# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = collections.deque([root])
        n = 0
        while len(q) > 0:
            l = len(q)
            for _ in range(l):
                n += 1
                p = q.popleft()
                if p.right is not None:
                    q.append(p.right)
                if p.left is not None:
                    q.append(p.left)
        
        return n
