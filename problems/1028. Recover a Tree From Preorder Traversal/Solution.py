# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str):
        t = traversal
        # Since there is always at least one node, and we know the first node
        # Is the root, we can create it right away.
        # Also note the algorithm is at least O(n).
        
        v = t.split("-")[0]
        root = TreeNode(int(v))

        d = 0 # Depth

        self.run(root, t[len(v):], d)
        return root

    def run(self, p, t, d):
        while True:
            td = 0
            for c in t:
                if c == "-":
                    td += 1
                else:
                    v = t.split("-")[td]
                    break
            if td > d:
                if p.left == None:
                    p.left = TreeNode(int(v))
                    t = self.run(p.left, t[td+len(v):], td)
                else:
                    p.right = TreeNode(v)
                    t = self.run(p.right, t[td+len(v):], td)
            else:
                return t
