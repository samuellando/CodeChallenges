class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            columnNumber = columnNumber // 26
            print(r, columnNumber)
            s = chr(r + 65) + s

        return s
