# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        n = 0
        m = 0

        pa = headA
        while pa is not None:
            m += 1
            pa = pa.next
        
        pb = headB
        while pb is not None:
            n += 1
            pb = pb.next
        
        pa = headA
        pb = headB
        if m > n:
            for _ in range(m-n):
                pa = pa.next
        elif m < n:
            for _ in range(n-m):
                pb = pb.next

        while pa is not None:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        
        return None
        
