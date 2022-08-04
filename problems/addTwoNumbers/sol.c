/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int sum = 0;
    ListNode head = new ListNode(0);
    ListNode c = head;
    while (true) {
      if (l1 != null) {
        c.val += l1.val;
        l1 = l1.next;
      }
      if (l2 != null) {
        c.val += l2.val;
        l2 = l2.next;
      }
      if (l1 != null || l2 != null || c.val >= 10) {
        c.next = new ListNode(0);
        c.next.val = c.val / 10;
        c.val = c.val % 10;
        c = c.next;
      }
      else break;
    }
    return head;
  }
}
