# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def add(self, n, v, d, r):
        if d == 1:
            if r:
                i = TreeNode(v, None, n)
            else:
                i = TreeNode(v, n, None)
            return i
        if n == None:
            return None
        n.right = self.add(n.right, v, d - 1, True)
        n.left = self.add(n.left, v, d - 1, False)
        return n
            
    
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.add(root, val, depth, False)
        
