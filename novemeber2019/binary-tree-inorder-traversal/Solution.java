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
  public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> l = new LinkedList<Integer>();
    if (root != null) {
      l.addAll(inorderTraversal(root.left));
      l.add(root.val);
      l.addAll(inorderTraversal(root.right));
    }
    return l;
  }
}
