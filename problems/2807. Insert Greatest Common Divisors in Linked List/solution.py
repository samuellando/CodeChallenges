# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head.next
        pp = head

        while p != None:
            v = gcd(p.val, pp.val)
            n = ListNode(v, p)
            pp.next = n
            n.next = p
            pp = p
            p = pp.next
        
        return head
