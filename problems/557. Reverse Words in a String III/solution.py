class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x : x[::-1], s.split(" ")))
        

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("Hello, world"))
