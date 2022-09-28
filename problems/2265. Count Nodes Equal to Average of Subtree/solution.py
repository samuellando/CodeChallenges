# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None, avg=0):
        self.val = val
        self.left = left
        self.right = right
        self.avg = avg

class Solution:
    def compAvs(self, root):
        if root == None:
            return 0, 0, 0
        
        nr, sr, mr = self.compAvs(root.right)
        nl, sl, ml  = self.compAvs(root.left)
        
        n = nr + nl + 1
        s = sr + sl + root.val
        
        root.avg = s // n
        
        m = mr + ml + (1 if root.avg == root.val else 0)
        
        return (n, s, m)
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.compAvs(root)[2]
