# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        q = [root]
        d = [1]
        
        while len(q) > 0:
            p = q.pop(0)
            dp = d.pop(0)

            if p.right is None and p.left is None:
                return dp
            if p.right is not None:
                q.append(p.right)
                d.append(dp + 1)
            if p.left is not None:
                q.append(p.left)
                d.append(dp + 1)
