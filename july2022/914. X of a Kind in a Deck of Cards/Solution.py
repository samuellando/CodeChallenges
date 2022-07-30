class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        m = {}
        for i in deck:
            if not m.get(i):
                m[i] = 1
            else:
                m[i] = m[i]+1
        
        ans = list(m.values())[0]
        for v in m.values():
            if v != ans:
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.hasGroupsSizeX([1,2,2,3,3,1,1,2,3]))
