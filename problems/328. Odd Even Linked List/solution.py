# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        eh = None
        ep = None

        p = head
        t = None

        while p != None:
            if eh == None:
                eh = p.next
                ep = eh
            else:
                ep.next = p.next
                ep = ep.next
            
            if p.next is not None:
                p.next = p.next.next
            
            t = p
            p = p.next
        
        t.next = eh
        return head


