# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        nil = ListNode(0)
        
        while head.next != None:
            if head.next == nil:
                return True
            else:
                p = head.next
                head.next = nil
                head = p
