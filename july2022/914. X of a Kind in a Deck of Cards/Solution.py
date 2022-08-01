class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        m = {}
        for i in deck:
            if not m.get(i):
                m[i] = 1
            else:
                m[i] = m[i]+1

        # Check if GCD is >= 2.
        r = list(m.values())[0]
        for v in m.values():
            r = gcd(r,v)

        if r >= 2:
            return True
        else:
            return False


def gcd(a,b):
    if b == 0:
        return a;
    else:
        return gcd(b, (a % b));
