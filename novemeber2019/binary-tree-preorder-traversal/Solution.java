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
  public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> l = new LinkedList<Integer>();
    if (root != null) {
      l.addAll(preorderTraversal(root.left));
      l.add(0, root.val);
      l.addAll(preorderTraversal(root.right));
    }
    return l;
  }
}
