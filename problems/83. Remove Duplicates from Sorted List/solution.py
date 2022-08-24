# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  head == None:
            return head
        
        p = head.next
        prev = head
        
        while p != None:
            if p.val == prev.val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        
        return head
        
