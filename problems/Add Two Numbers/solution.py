# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # pointers
        p1 = l1
        p2 = l2
        
        res = None
        pr = res
        
        carry = 0
        while p1 != None or p2 != None:
            s = carry
            if p1 is not None:
                s += p1.val
                p1 = p1.next
            if p2 is not None:
                s += p2.val
                p2 = p2.next
            
            if pr is None:
                res = ListNode(s % 10)
                pr = res
            else:
                pr.next = ListNode(s%10)
                pr = pr.next
            
            carry = s // 10
        
        if carry > 0:
            pr.next = ListNode(carry)
        
        return res
            
