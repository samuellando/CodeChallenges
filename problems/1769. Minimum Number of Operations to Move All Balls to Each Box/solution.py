class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        o = [0] * len(boxes)

        r = 0

        for i, s in enumerate(boxes):
            if s == "1":
                o[0] += i
                r += 1
        
        if boxes[0] == "1":
            r -= 1

        l = 0

        for i in range(1, len(o)):
            o[i] = o[i-1] - r + l
            if boxes[i-1] == "1":
                l += 1
                o[i] += 1
            if boxes[i] == "1":
                r -= 1

        return o
