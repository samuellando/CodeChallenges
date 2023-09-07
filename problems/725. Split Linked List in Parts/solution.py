# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k

        l = 0
        p = head
        while p is not None:
            l += 1
            p = p.next
        
        pl = l // k
        r = l - pl * k

        phead = head
        for i in range(k):
            res[i] = phead
            if phead is None:
                break

            if r > 0:
                l = pl + 1
                r -= 1
            else: 
                l = pl

            print(l)
            p = phead
            for _ in range(1, l):
                if p is not None:
                    p = p.next
            
            if p is not None:
                phead = p.next
                p.next = None
            else:
                phead = None

        return res


