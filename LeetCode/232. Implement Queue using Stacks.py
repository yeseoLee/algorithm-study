class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x: int) -> None:
        if self.s1:
            self.s2.append(x)
            while self.s1:
                self.s2.append(self.s1.pop(-1))
        else:
            self.s1.append(x)
            while self.s2:
                self.s1.append(self.s2.pop(-1)) 

    def pop(self) -> int:
        if self.s1:
            return self.s1.pop(-1)
        else:
            return self.s2.pop(-1)

    def peek(self) -> int:
        if self.s1:
            return self.s1[-1]
        else:
            return self.s2[-1]
        
    def empty(self) -> bool:
        return (not self.s1 and not self.s2)
