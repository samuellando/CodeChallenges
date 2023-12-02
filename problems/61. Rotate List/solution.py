# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the length
        l = 0
        p = head
        while p is not None:
            l += 1
            p = p.next

        if l <= 1 or k == 0:
            return head
        
        # Get the index of the next tail
        i = (l - k - 1) % l
        
        # If it's the same tail, just return head.
        if i == l - 1:
            return head

        # Move to the new tail
        p = head
        for _ in range(i):
            p = p.next
        
        # The new head is the next value.
        head2 = p.next
        # cut off at the tail
        p.next = None

        # Move to the end of the splice
        p = head2
        while p.next is not None:
            p = p.next
        
        # connect to the original head
        p.next = head

        return head2
