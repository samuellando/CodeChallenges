class Solution:
    def reverseBits(self, n: int) -> int:
        s = "{:b}".format(n)
        s = "0" * (32 - len(s)) + s
        return int(s[::-1],2)
