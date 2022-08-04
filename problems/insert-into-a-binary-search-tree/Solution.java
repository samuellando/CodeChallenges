/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
  public TreeNode insertIntoBST(TreeNode root, int val) {
    TreeNode n = new TreeNode(val);
    TreeNode t = root;
    while (true) {
      if (t.val < val)
        if (t.right == null) {
          t.right = n;
          break;
        } else
          t = t.right;
        else 
          if (t.left == null) {
            t.left = n;
            break;
          } else 
            t = t.left;
    }
    return root;
  }
}
