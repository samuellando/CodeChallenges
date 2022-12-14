# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return s(root, False, False)


def s(r, p, g):
    if r is None:
        return 0
    
    v = s(r.right, r.val % 2 == 0, p)
    v += s(r.left, r.val % 2 == 0, p)

    if g:
        return r.val + v
    else:
        return v
