class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k + 1
        self.s = [None] * self.k
        self.f = self.k - 1
        self.r = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.f = (self.f + 1) % self.k
        self.s[self.f] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.r = (self.r - 1 + self.k) % self.k
        self.s[self.r] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f - 1 + self.k) % self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.r = (self.r + 1) % self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[self.r]

    def isEmpty(self) -> bool:
        return (self.f + 1) % self.k == self.r

    def isFull(self) -> bool:
        return (self.f + 2) % self.k == self.r
