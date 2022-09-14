class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        io = []
        stack = []
        p = root
        d = 1
        # since |val| <= 100, propend with depth at the 1000s place.
        # check that the inorder traversal, with depths, is palendromic.
        while len(stack) > 0 or p != None:
            if p == None:
                p = stack.pop(0)
                io.append(p.val)
                d = (-1 if p.val < 0 else 1)*p.val // 1000
                d += 1
                p = p.right
                
                
            else:
                p.val = (-1 if p.val < 0 else 1)*d*1000 + p.val
                stack.insert(0, p)
                d += 1
                p = p.left
            
        for i in range(len(io) // 2 + 1):
            if io[i] != io[(-1*i) - 1]:
                return False
            
            
        return True
