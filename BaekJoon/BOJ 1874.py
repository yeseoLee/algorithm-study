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
    def clear(self):
        self.stack=[]
s=Stack()
n=int(sys.stdin.readline())
a=[]
b=[]
for i in range(n):
    tmp=(int(sys.stdin.readline()))
    a.append(tmp)
j=0
for i in range(1,n+1):
    if(i<=a[j]):
        s.push(i)
        b.append("+")      
    while(s.peak()==a[j]):
        s.pop()
        b.append("-")
        j+=1
        if(j==n): break

if not s.isEmpty():
    print("NO")
else:
    for i in b:
        print(i)
