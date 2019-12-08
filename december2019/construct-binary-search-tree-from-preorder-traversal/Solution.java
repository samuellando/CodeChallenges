import java.util.Stack;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
}


class Solution {
  public static TreeNode bstFromPreorder(int[] preorder) {
    if (preorder.length == 0)
      return null;

    TreeNode root = new TreeNode(preorder[0]);

    Stack<TreeNode> parents = new Stack<TreeNode>();
    parents.push(root);
    TreeNode n;
    TreeNode p;
    for (int i = 1; i < preorder.length; i++) {
      n = new TreeNode(preorder[i]);
      if (n.val < parents.peek().val) {
        parents.peek().left = n;
        parents.push(n);
      }
      else {
        p = parents.peek();
        while (!parents.isEmpty() && parents.peek().val < n.val)
          p = parents.pop();
        p.right = n;
        parents.push(n);
      }
    }
    return root;
  }

  public static void main(String[] args) {
    int[] p = {8,5,1,7,10,12};
    bstFromPreorder(p);
  }
}
