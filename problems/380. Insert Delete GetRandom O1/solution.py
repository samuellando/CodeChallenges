import random

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []
        
    def insert(self, val: int) -> bool:
        if self.d.get(val) is None:
            self.l.append(val)
            self.d[val] = len(self.l) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.d.get(val) is not None:
            last = self.l[-1]
            self.d[last] = self.d[val]
            self.l[self.d[val]] = last
            del self.l[-1]
            del self.d[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        r = random.randint(0, len(self.l) - 1)
        return self.l[r]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
