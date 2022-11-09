class StockSpanner:

    def __init__(self):
        self.s = []
        self.i = 0
        
    def next(self, price: int) -> int:
        self.i += 1
        if len(self.s) > 0 and self.s[-1][1] > price:
            d = 1
        else:
            while len(self.s) > 0 and self.s[-1][1] <= price:
                self.s = self.s[:-1]
        
            if len(self.s) == 0:
                d =  self.i
            else:
                d = self.i - self.s[-1][0]
        
        self.s.append([self.i, price])
        return d
        
            
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
