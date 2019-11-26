/**
  * Definition for a binary tree node.
  * public class TreeNode {
  *     int val;
  *     TreeNode left;
  *     TreeNode right;
  *     TreeNode(int x) { val = x; }
  * }
  */

import java.util.LinkedList;

class Solution {
  public TreeNode bstToGst(TreeNode root) {
    int sum = sum(root);
    List<TreeNode> traversal = inorderTraversal(root);

    int oldVal;
    for (TreeNode n:traversal) {
      oldVal = n.val;
      n.val = sum;
      sum -= oldVal;
    }
    return root;
  }

  public List<TreeNode> inorderTraversal(TreeNode root) {
    List<TreeNode> l = new LinkedList<TreeNode>();
    if (root != null) {
      l.addAll(inorderTraversal(root.left));
      l.add(root);
      l.addAll(inorderTraversal(root.right));
    }
    return l;
  }

  private int sum(TreeNode t) {
    if (t == null) return 0;
    else return t.val + sum(t.right) + sum(t.left);
  }
}
