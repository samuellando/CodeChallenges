# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = self.reversen(head, k)
        p = head
        
        while p.next != None:
            tmp = p.next
            p.next = self.reversen(tmp, k)
            p = tmp
        
        return newHead
        
    def reversen(self, head, k):
        p = head
        stk = []
    
        for i in range(k):
            if p == None:
                return head
            stk.insert(0, p)
            p = p.next
        
        newHead = stk[0]
        after = stk[0].next
        
        while len(stk) > 1:
            p = stk.pop(0)
            p.next = stk[0]
        
        stk[0].next = after
        
        return newHead
