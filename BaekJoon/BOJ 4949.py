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
while(True):
    line=sys.stdin.readline()
    line=line[:-1]
    if(line=="."):
        break
    for i in line:
        if(i=="["or i=="("):
            s.push(i)
        elif(i=="]"):
            if(s.peak()=="["):
                s.pop()
            else:
                s.push(1)
                break
        elif(i==")"):
            if(s.peak()=="("):
                s.pop()
            else:
                s.push(1)
                break
    if s.isEmpty():
        print("yes")
    else:
        print("no")
        s.clear()
