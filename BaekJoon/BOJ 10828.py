import sys

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not (self.empty()):
            return self.stack.pop(-1)
        else:
            return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        if(self.size()==0): return 1
        else: return 0
    def top(self):
        if not (self.empty()):
            return self.stack[-1]
        else:
            return -1

s=Stack()
n=int(sys.stdin.readline())
for i in range(n):
    line=sys.stdin.readline().split()
    if(line[0]=="push"):
        s.push(line[-1])
    elif(line[0]=="pop"):
        print(s.pop())
    elif(line[0]=="size"):
        print(s.size())
    elif(line[0]=="empty"):
        print(s.empty())
    elif(line[0]=="top"):
        print(s.top())
    else:
        print("입력오류")
