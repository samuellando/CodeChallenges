# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def bal(r, d):
    if r is None:
        return 0
        
    if r.left is not None:
        dl = bal(r.left, d + 1)
    else:
        dl = d
    
    if r.right is not None:
        dr = bal(r.right, d + 1)
    else:
        dr = d
    
    if abs(dl - dr) > 1 or dl == -1 or dr == -1:
        return -1
    else:
        return max(dl, dr)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return bal(root, 0) >= 0
        
