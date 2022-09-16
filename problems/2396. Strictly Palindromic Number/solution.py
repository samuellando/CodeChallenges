class Solution:
    def toBase(self, n, b):
        if n == 0:
            return [0]
        
        digits = []
        while n > 0:
            digits.append(int(n % b))
            n //= b
        
        return digits[::-1]
        
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n-1):
            digits = self.toBase(n,b)
            for i in range(len(digits) // 2):
                if digits[i] != digits[-1*i-1]:
                    return False
        
        return True
        
