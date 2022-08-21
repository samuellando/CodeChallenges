class Solution:
    def generateParenthesis(self, n: int):
         """
         keep track of the number of open and closes.
         In the call stack.

         if o == n, make c == n
         if o < n and c == o, add o
         if o < n and c < o, fork:
            add another o
            OR add c

         these are the only values that matter for state.
         """
         return self.run(o, c, n)

    def run(self,o, c, n):
        l = []
        if o == n:
            return [")" * (n-c)]
        else: # o < n
            if c == o:
                l.extend(self.run(o+1, c, n))
                l = ["("+s for s in l]
            else:
                # Fork.
                l2 = l.copy()
                l.extend(self.run(o+1, c, n))
                l = ["("+s for s in l]

                l2.extend(self.run(o, c+1, n))
                l2 = [")"+s for s in l2]
                l.extend(l2)


        return l

if __name__ == "__main__":
    s = Solution()
    print(s.run(0, 0, 3))


