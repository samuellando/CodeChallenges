# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root == None:
            return res
        
        s = [root] # The stack
        
        while len(s) > 0:
            p = s.pop()
            
            if p.right == None and p.left == None:
                res.append(p.val)
            else:
                if p.right != None:
                    s.append(p.right)
                s.append(p)
                if p.left != None:
                    s.append(p.left)
                
                p.right = None
                p.left = None
        
        return res
