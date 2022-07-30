# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        c1 = head
        p = head.next

        s = 0

        while p != None:
            if p.val == 0:
                n = ListNode(s, p)
                c1.next = n
                c1 = p
                s = 0
            else:
                s = s + p.val
            p = p.next

        return head
        

if __name__ == "__main__":
    n0 = ListNode(0)
    n = ListNode(1, n0)
    n1 = ListNode(0, n)
    n23 = ListNode(7, n1)
    n22 = ListNode(5, n23)
    n21 = ListNode(4, n22)
    n2 = ListNode(0, n21)
    n32 = ListNode(5, n2)
    n3 = ListNode(1, n32)
    n4 = ListNode(0, n3)
    n5 = ListNode(1, n4)
    n6 = ListNode(0, n5)

    ni = n5
    while ni != None:
        print(ni.val)
        ni = ni.next

    print("OK")

    s = Solution()
    n9 = s.mergeNodes(n6)

    ni = n9
    while ni != None:
        print(ni.val)
        ni = ni.next

