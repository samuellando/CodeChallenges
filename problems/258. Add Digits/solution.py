class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            s = 0
            while num > 0:
                s += num % 10
                num = num // 10
            num = s
        return num
