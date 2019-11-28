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
  public TreeNode constructMaximumBinaryTree(int[] nums) {
    return constructMaximumBinaryTree(nums, 0, nums.length-1);
  }
  private TreeNode constructMaximumBinaryTree(int[] nums, int start, int end) {
    if (end < start)
      return null;
    int max = start;
    for (int i = start + 1; i <= end; i++)
      if (nums[i] > nums[max])
        max = i;
    TreeNode t = new TreeNode(nums[max]);
    t.left = constructMaximumBinaryTree(nums, start, max-1);
    t.right = constructMaximumBinaryTree(nums, max+1, end);
    return t;
  }
}
