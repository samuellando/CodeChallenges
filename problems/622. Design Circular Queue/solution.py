class Node:
    def __init__(self, v):
        self.v = v
        self.n = None
        self.b = None


class MyCircularQueue:

    def __init__(self, k: int):
        nodes = [] 
        
        for i in range(k):
            nodes.append(Node(None))

        for i in range(k-1):
            nodes[i].n = nodes[i+1]
        nodes[-1].n = nodes[0]

        for i in range(k-1, 0, -1):
            nodes[i].b = nodes[i-1]
        nodes[0].b = nodes[-1]

        self.p = nodes[0]
        self.r = nodes[0]
        self.l = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.p.v == None:
            self.r = self.p.b

        self.p = self.p.b
        
        if self.p.v == None:
            self.l += 1
        elif self.r == self.p:
            self.r = self.p.n

        self.p.v = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.r.v = None
        self.r = self.r.b
        if self.l > 0:
            self.l -= 1
        return True

    def Front(self) -> int:
        if self.r.v == None:
            return -1
        return self.r.v

    def Rear(self) -> int:
        if self.p.v == None:
            return -1
        return self.p.v

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k
