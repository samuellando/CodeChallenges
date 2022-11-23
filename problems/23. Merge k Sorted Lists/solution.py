# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        o = ListNode(0, None)
        p = o
        
        # Use a stack to reduce the number of comparisons
        h = []
        heapq.heapify([h])
        
        for i, l in enumerate(lists):
            if l != None:
                heapq.heappush(h, (l.val, i, l))
                
        while len(h) > 0:
            n = heapq.heappop(h)
            p.next = ListNode(n[0])
            p = p.next
            if not n[2].next is None:
                l = n[2].next
                heapq.heappush(h, (l.val, n[1], l))
            
        
        return o.next
