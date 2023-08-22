# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        # Do a BFS
        
        q = [root]
        res = [[root.val]]
        
        level = 0 # Keep track of the level so we can reverse when wee need to.
        while len(q) > 0:
            n = len(q) # Number of nodes at this level
            # Load the next level
            vals = []
            level += 1
            for _ in range(n):
                p = q.pop(0)
                
                if p.left != None:
                    vals.append(p.left.val)
                    q.append(p.left)
                    
                if p.right != None:
                    vals.append(p.right.val)
                    q.append(p.right)
            
            # Flip the vals if we need to.
            if level % 2 == 1:
                vals.reverse()
            
            if len(vals) > 0:
                res.append(vals)
        
        return res
