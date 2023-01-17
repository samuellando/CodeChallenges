# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        s = [root]
        sums = [root.val]

        while len(s) > 0:
            p = s.pop()
            ps = sums.pop()

            if p.left is None and p.right is None and ps == targetSum:
                return True
            
            if p.left is not None:
                s.append(p.left)
                sums.append(p.left.val + ps)
            
            if p.right is not None:
                s.append(p.right)
                sums.append(p.right.val + ps)

        return False
