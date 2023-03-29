class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        p = 0
        columnTitle = columnTitle[::-1]
        for c in columnTitle:
            n = ord(c) - 64
            ans += n * pow(26, p)
            p += 1
        
        return ans


