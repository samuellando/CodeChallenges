class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
}

class Solution {
    public static boolean isValidBST(TreeNode root) {
        TreeNode p = new TreeNode(0);
        p.left = new TreeNode(0);
        return isValidBST(root, p);
    }
    
    public static boolean isValidBST(TreeNode r, TreeNode p) {
        if (r == null)
            return true;
        if (!(isValidBST(r.left, p)))
            return false;
        if (p.left == null && p.val >= r.val)
            return false;
        p.val = r.val;
        p.left = null;
        return isValidBST(r.right, p); 
    }
}