import sys
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size()==0
    def clear(self):
        self.stack=[]
s=Stack()
t=int(sys.stdin.readline())
for i in range(t):
    line=sys.stdin.readline()
    line=line[:-1]
    for i in line:
        if(i=='('):
            s.push(i)
        else:
            if(s.isEmpty()):
                s.push(1)
                break
            else:
                s.pop()
    if s.isEmpty():
        print("YES")
    else:
        print("NO")
    s.clear()
        
        
        
