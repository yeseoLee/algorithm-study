import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def empty(self):
        if not self.head: return 1
        else: return 0
    def enqueue(self,data):
        newNode=Node(data)
        if self.empty():
            self.head=newNode
            self.tail=newNode
        self.tail.next=newNode
        self.tail=newNode
        self.size+=1
    def dequeue(self):
        if self.empty():
            return -1
        elif self.size==1:
            result=self.head.data
            self.head=None
            self.tail=None
            self.size=0
            return result
        else:
            result=self.head.data
            self.head=self.head.next
            self.size-=1
            return result
            
que=Queue()
n=int(sys.stdin.readline())
for i in range(n):
    line=sys.stdin.readline().split()
    if(line[0]=='push'):
        que.enqueue(line[1])
    elif(line[0]=='pop'):
        print(que.dequeue())
    elif(line[0]=='size'):
        print(que.size)
    elif(line[0]=='empty'):
        print(que.empty())
    elif(line[0]=='front'):
        if(que.empty()):
            print(-1)
        else:
            print(que.head.data)
    elif(line[0]=='back'):
        if(que.empty()):
            print(-1)
        else:
            print(que.tail.data)

"""
리스트로 큐를 구현하니 pop 에서 O(n)의 시간이 소요되어 시간 초과
해결방법 1. 연결리스트로 큐를 구현
해결방법 2. 리스트에서 pop 대신 시작인덱스를 1씩 더하며 큐를 왼쪽으로 옮김
해결방법 3. collections deque 사용
"""

