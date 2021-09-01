#1. Using 2 Queue
class MyStack:
    def __init__(self):
        self.que1=deque([])
        self.que2=deque([])

    def push(self, x: int) -> None:
        if self.que1:
            self.que2.append(x)
            while(self.que1):
                self.que2.append(self.que1.popleft())
        else :
            self.que1.append(x)
            while(self.que2):
                self.que1.append(self.que2.popleft())

    def pop(self) -> int:
        if self.que1:
            return self.que1.popleft()
        elif self.que2:
            return self.que2.popleft()
        else:
            return None
        
    def top(self) -> int:
        if self.que1:
            return self.que1[0]
        elif self.que2:
            return self.que2[0]
        else:
            return None

    def empty(self) -> bool:
        return (not self.que1 and not self. que2)

#2.  push x and sorting the others
class MyStack:

    def __init__(self):
        self.que=collections.deque([])
        
    def push(self, x: int) -> None:
        self.que.append(x)
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())

    def pop(self) -> int:
        return self.que.popleft()
        
    def top(self) -> int:
        return self.que[0]
        
    def empty(self) -> bool:
        return not self.que
