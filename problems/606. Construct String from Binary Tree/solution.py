# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.run(root)
    
    def run(self, n, ):
        s = str(n.val)
        if n.left != None:
            s += "(" + self.run(n.left) + ")"
        else:
            if n.right != None:
                s += "()"
        if n.right != None:
            s += "(" + self.run(n.right) + ")"
        return s
