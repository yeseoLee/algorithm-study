class MyCircularQueue:
    def __init__(self, k: int):
        self.len=k+1
        self.cq=[0]*self.len
        self.front=0
        self.rear=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear+1) % self.len
            self.cq[self.rear]=value
            return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % self.len
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[(self.front+1) % self.len]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[self.rear]

    def isEmpty(self) -> bool:
        return self.front==self.rear

    def isFull(self) -> bool:
        return (self.rear+1)%self.len == self.front
