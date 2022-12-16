class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        t = []
        while len(self.s) > 0:
            t.insert(0, self.s.pop(0))
        self.s.insert(0, x)
        
        while len(t) > 0:
            self.s.insert(0, t.pop(0))
    
    def pop(self) -> int:
        return self.s.pop(0)
        
    def peek(self) -> int:
        return self.s[0]
        

    def empty(self) -> bool:
        return len(self.s) == 0
