# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def d(self, n, d):
        if n == None:
            return d
        else:
            return max(self.d(n.right, d), self.d(n.left, d)) + 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.d(root, 0)
