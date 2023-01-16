class MyQueue:

    def __init__(self):
        self.queue = []  # 1
        self.p = []  # 2

    def push(self, x: int) -> None:
        while self.queue:
            self.p.append(self.queue.pop())
        self.queue.append(x)
        while self.p:
            self.queue.append(self.p.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
