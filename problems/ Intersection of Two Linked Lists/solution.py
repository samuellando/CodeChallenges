class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        
        i = None
        
        # Fist ghet the length of each list
        la = 0
        while pa is not None:
            la += 1
            pa = pa.next
            
        lb = 0
        while pb is not None:
            lb += 1
            pb = pb.next
        
        pa = headA
        pb = headB
        
        # Now skip, and move through each to find the interesction.
        
        if la > lb:
            skip = la - lb
            for _ in range(skip):
                pa = pa.next
        elif lb > la:
            skip = lb - la
            for _ in range(skip):
                pb = pb.next
        
        print(pa.val, pb.val)
        i = None
        while pa is not None:
            if pa == pb:
                i = pa 
                break
            else:
                pa = pa.next
                pb = pb.next
        
        return i
