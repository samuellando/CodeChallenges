# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head
        
        head_even = None
        head_odd = None
        p_odd = None
        p_even = None
        
        i = 1
        while p is not None:
            if i % 2 == 0:
                if p_even is None:
                    head_even = p
                    p_even = p
                else:
                    p_even.next = p
                    p_even = p
            else:
                if p_odd is None:
                    head_odd = p
                    p_odd = p
                else:
                    p_odd.next = p
                    p_odd = p
            
            pt = p.next
            p.next = None
            p = pt
            i += 1
        
        if head_odd is None:
            return head_even
        else:
            p_odd.next = head_even
            return head_odd
