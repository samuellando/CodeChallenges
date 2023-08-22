# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.bt(preorder, inorder, 0, 0, len(inorder))[0]

    def bt(self, po, io, i, s, e):
        if s == e:
            return (TreeNode(po[i]), i)
        
        # Get left and right
        pos = None
        for j in range(s, e):
            if po[i] == io[j]:
                pos = j
                break
        
        left = None
        right = None
        imax = i
        if pos > s:
            left, imax = self.bt(po, io, i+1, s, pos)
    
        if pos < e-1:
            right, imax = self.bt(po,io,imax + 1,pos+1,e)
        
        return (TreeNode(po[i], left, right), imax)
