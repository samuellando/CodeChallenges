# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.r(root)
        
        if root.val == 0 and root.left == None and root.right == None:
            return None
        else:
            return root
    
    def r(self, root):
        l1 = False
        r1 = False
        
        if root.left != None:
            l1 = self.r(root.left)
        if root.right != None:
            r1 = self.r(root.right)
        
        if not l1:
            root.left = None
        if not r1:
            root.right = None
            
        return l1 or r1 or root.val == 1
