class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        sm1 = 1
        sm2 = 1
        for i in range(1, n):
            sm1 = sm1 + sm2
            sm2 = sm1 - sm2

        return sm1

        
