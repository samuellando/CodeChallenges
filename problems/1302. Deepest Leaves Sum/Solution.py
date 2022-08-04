def getDepthSums(m, d, root):
    if d in m:
        m[d] += root.val
    else:
        m[d] = root.val

    if root.right != None:
        getDepthSums(m, d+1,root.right)

    if root.left != None:
        getDepthSums(m, d+1,root.left)


class Solution:
        def deepestLeavesSum(self, root) -> int:
            # Given the structure, this is at least O(n).
            
            m = {} # Map aggregator for sum at each depth.

            getDepthSums(m, 0, root)

            return list(m.values())[-1] # The last value will always be max depth
