import sys
class queue():
    def __init__(self):
        self.que=[]
    def push(self,x):
        self.que.append(x)
    def pop(self):
        if(len(self.que)):
            return self.que.pop(0)
        else:
            return -1
    def size(self):
        return len(self.que)
    def empty(self):
        return 0 if(len(self.que)) else 1
    def front(self):
        if(len(self.que)):
            return self.que[0]
        else:
            return -1
    def back(self):
        if(len(self.que)):
            return self.que[-1]
        else:
            return -1
Que=queue()
n=int(sys.stdin.readline())
for i in range(n):
    command=list(sys.stdin.readline().split())
    if(command[0]=='push'):
        Que.push(int(command[1]))
    elif(command[0]=='pop'):
        print(Que.pop())
    elif(command[0]=='size'):
        print(Que.size())
    elif(command[0]=='empty'):
        print(Que.empty())
    elif(command[0]=='front'):
        print(Que.front())
    elif(command[0]=='back'):
        print(Que.back())
    else:
        print("error")
