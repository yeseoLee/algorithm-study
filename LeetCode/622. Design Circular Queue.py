from collections import deque


# 3 ms / 18.65 MB
class MyCircularQueueByQueue:
    def __init__(self, k: int):
        self.que = deque()
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.que.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[-1]

    def isEmpty(self) -> bool:
        return len(self.que) == 0

    def isFull(self) -> bool:
        return len(self.que) == self.k


# 1 ms / 18.46 MB
class MyCircularQueueByArray:
    def __init__(self, k: int):
        self.que = [-1] * k
        self.k = k
        self.f = 0
        self.r = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.r = (self.r + 1) % self.k
        self.que[self.r] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.que[self.f] = -1
        self.f = (self.f + 1) % self.k
        return True

    def Front(self) -> int:
        return self.que[self.f]

    def Rear(self) -> int:
        return self.que[self.r]

    def isEmpty(self) -> bool:
        return self.que[self.f] == -1

    def isFull(self) -> bool:
        return self.que[self.r] != -1 and (self.r + 1) % self.k == self.f
