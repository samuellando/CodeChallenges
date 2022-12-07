# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = [root]
        o = 0

        while len(s) > 0:
            p = s.pop(0)

            if p.val >= low and p.val <= high:
                o += p.val
            
            if p.right is not None:
                s.insert(0, p.right)
            if p.left is not None:
                s.insert(0, p.left)
        
        return o
