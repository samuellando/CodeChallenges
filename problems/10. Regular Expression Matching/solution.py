class NDFANode():
    def __init__(self, val, star):
        self.val = val
        self.star = star
        self.next = []
        if star:
            self.next.append(self)
    
    def equal(self, other):
        return self.star and other.star and self.val == other.val

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Build a NDFA for the regEx
        head = NDFANode("start", False)
        prev = head
        for i, c in enumerate(p):
            if c == "*":
                continue

            star = False
            if i < len(p) - 1 and p[i+1] == "*":
                star = True
            n = NDFANode(c, star)

            for ne in prev.next:
                if not ne.equal(n):
                    ne.next.append(n)
            if not prev.equal(n):
                prev.next.append(n)
            if not star:
                prev = n

        end = NDFANode("end", False)
        for ne in prev.next:
            ne.next.append(end)
        prev.next.append(end)
        # Test against the NDFA
        return match(s, head)

def match(s, node):
    print(s, node.val)
    if len(s) == 0:
        if node.val == "end":
            return True
    else:
        if node.val == "start":
            for n in node.next:
                if match(s, n):
                    return True
        elif node.val == s[0] or node.val == ".":
            for n in reversed(node.next):
                if match(s[1:], n):
                    return True
    
    return False
