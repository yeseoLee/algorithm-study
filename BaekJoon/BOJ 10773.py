import sys
class Stack:
    def __init__ (self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size==0

s=Stack()
Sum=0
k=int(sys.stdin.readline())
for i in range(k):
    tmp=int(sys.stdin.readline())
    if(tmp!=0):
        s.push(tmp)
    else:
        s.pop()
    
while(s.isEmpty()==False):
    Sum+=s.pop()
print(Sum)
    
