# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def toTree(n):
    if len(n) == 0:
        return

    p = len(n) // 2
    root = TreeNode(n[p], toTree(n[:p]), toTree(n[p+1:]))

    return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        r =  toTree(nums)
        return r
        
