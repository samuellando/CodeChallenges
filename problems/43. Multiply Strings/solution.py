class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = []
        
        zeros = 0
        for i in num1[::-1]:
            carry = 0
            s = ""
            for j in num2[::-1]: 
                s = str((int(i) * int(j) + carry) % 10) + s
                carry = (int(i) * int(j) + carry) // 10
            if carry > 0:
                s = str(carry) + s
            a.append(s + "0" * zeros)
            zeros += 1
        
        result = ""
        carry = 0
        for i in range(len(a[-1])):
            s = 0
            for n in a:
                if len(n) > i:
                    s += int(n[len(n) - 1 - i])
            result = str((s + carry) % 10) + result
            carry = (s + carry) // 10
        if carry > 0:
            result = str(carry) + result
                
        while len(result) > 1:
            if result[0] == "0":
                result = result[1:]
            else:
                break
            
        return str(result)
