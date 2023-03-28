class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        neg = False

        if dividend < 0:
            neg = True

            dividend = abs(dividend)
        
        if divisor < 0:
            if neg:
                neg = False
            else: 
                neg = True
            
            divisor = abs(divisor)
        
        ans = len(range(0, dividend-divisor+1, divisor))
        
        if neg:
            ans = -ans
        
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)

        return min(max(ans, minus_limit), plus_limit)
