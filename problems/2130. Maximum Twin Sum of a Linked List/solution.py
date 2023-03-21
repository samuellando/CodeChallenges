# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        s = []

        n = 0
        p = head
        while p != None:
            p = p.next
            n += 1
        
        p = head
        for i in range(n/2):
            s.append(p.val)
            p = p.next
        
        m = 0
        for i in range(n/2):
            t = s.pop() + p.val
            if t > m:
                m = t
            
            p = p.next
        
        return m
