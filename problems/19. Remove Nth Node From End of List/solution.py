# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:    
        p = head
        d = head
        
        for i in range(n):
            p = p.next
        
        if p == None:
            return head.next
            
        while p.next != None:
            d = d.next
            p = p.next
            
        d.next = d.next.next
        
        return head
