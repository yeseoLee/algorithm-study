from collections import deque


# 3 ms / 17.88 MB
class MyStack:
    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        while True:
            if len(self.que1) == 1:
                target = self.que1.popleft()
                break
            self.que2.append(self.que1.popleft())
        self.que1 = self.que2
        self.que2 = deque()

        return target

    def top(self) -> int:
        if self.empty():
            return None
        while True:
            if len(self.que1) == 1:
                target = self.que1.popleft()
                self.que2.append(target)
                break
            self.que2.append(self.que1.popleft())
        self.que1 = self.que2
        self.que2 = deque()
        return target

    def empty(self) -> bool:
        return len(self.que1) == 0
