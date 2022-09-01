# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.check(root.left, root.val) + self.check(root.right, root.val)
    
    def check(self, root,  val):
        if root == None:
            return 0
        if root.val >= val:
            c = 1
            print(root.val, "is good")
        else:
            c = 0
        if root.val > val:
            val = root.val
        return c + self.check(root.left, val) + self.check(root.right, val)
