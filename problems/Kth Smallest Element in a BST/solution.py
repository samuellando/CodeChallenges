# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # An in order traversal of a BTS is always in order.
        
        # Do a DFS, in order traversal
        current = root
        s = []
        
        i = 1
        while True:
            if current != None:
                s.append(current)
                current = current.left
            elif len(s) > 0:
                current = s.pop()
                if i == k:
                    return current.val
                else:
                    i += 1
                current = current.right
            else: break
            
