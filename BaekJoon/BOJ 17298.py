import sys
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)
    def peak(self):
        if not self.isEmpty():
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size()==0

s1=Stack()
s2=Stack()

n=int(sys.stdin.readline())
line=list(map(int,sys.stdin.readline().split()))
NGE=[0]*n
for i in line:
    s1.push(i)

for i in range(n-1,-1,-1):
    while(not s2.isEmpty()):
        if(s1.peak()<s2.peak()): break
        else: s2.pop()
    if(s2.isEmpty()):
        NGE[i]=-1
    else:
        NGE[i]=s2.peak()
    s2.push(s1.pop())

for i in NGE:
    print(i,end=" ")
