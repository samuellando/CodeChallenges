# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        p = head
        while p != None:
            if p.val == val:
                if prev == None:
                    head = p.next
                else:
                    prev.next = p.next
            else:
                prev = p
            p = p.next
            
                                
        return head
