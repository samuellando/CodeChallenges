import java.util.LinkedList;
import java.util.List;

class Solution {
  public static void main(String[] args) {
    int[] nums = {1,2,3};
    Solution s = new Solution();
    List<List<Integer>> p = s.permute(nums);
  }

  private int factorial(int n) {
    int ac = 1;
    while (n > 1) {
      ac *= n;
      n--;
    }
    return ac;
  }

  public List<List<Integer>> insert(List<List<Integer>> p, int n) {
    List<List<Integer>> pn = new LinkedList<List<Integer>>();
    Integer no = new Integer(n);
    for (int i = 0; i < p.size(); i++)
      for (int j = 0; j < p.get(i).size(); j++) {
        pn.addAll(new LinkedList(p.get(i)));
        pn.get(p.get(i).size()*i + j).add(j, no);
      }
    return pn;
  }

  public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> p = new LinkedList<List<Integer>>();
    if (nums.length == 0)
      return p;

    p.add(new LinkedList<Integer>());
    p.get(0).add(new Integer(nums[0]));
    for (int i = 1; i < nums.length; i++)
      p = insert(p, nums[i]);
    return p;
  }
}
