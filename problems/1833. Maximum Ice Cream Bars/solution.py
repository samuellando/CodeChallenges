class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        c = 0
        for b in costs:
            if coins < b:
                break
            else:
                coins -= b
                c += 1
        
        return c
