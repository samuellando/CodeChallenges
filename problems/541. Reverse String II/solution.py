class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = [s[i:(i+k if i+k < len(s) else len(s))] for i in range(0, len(s), k)]
        return ''.join([(l[i][::-1] if i % 2 == 0 else l[i]) for i in range(len(l))])

if __name__ == "__main__":
    s = Solution()
    print(s.reverseStr("abcded", 2))
