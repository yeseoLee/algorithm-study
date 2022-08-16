from heapq import heappush, heappop
import sys
input = sys.stdin.readline

class DoubleQue:
    def __init__(self):
        self.max_que = []
        self.min_que = []
        self.id = [0] * 1000000
        
    def is_empty(self):
        return len(self.max_que)==0

    def sync(self,num):
        if num==1:
            arr = self.max_que
        else:
            arr = self.min_que
        while arr and self.id[arr[0][1]] == 0:
            heappop(arr)
            
    def insert(self,num,idx):
        heappush(self.max_que,(-num,idx))
        heappush(self.min_que,(num,idx))
        self.id[idx] = 1
        
    def delete(self,num):
        self.sync(num)

        if num == 1 and self.max_que:
            self.id[self.max_que[0][1]] = 0
            heappop(self.max_que)
        elif num == -1 and self.min_que:
            self.id[self.min_que[0][1]] = 0
            heappop(self.min_que)
            
    def print(self):
        self.sync(1)
        self.sync(-1)
        if self.is_empty():
            print("EMPTY")
        else:
            print(-heappop(self.max_que)[0],heappop(self.min_que)[0])

    def debug(self):
        print("DEBUGING")
        print("______________")
        print(self.max_que)
        print(self.min_que)
        print("______________")
        
T=int(input())
for case in range(T):
    dq = DoubleQue()
    k=int(input())
    for idx in range(k):
        cmd,num = input().split()
        num = int(num)
        if cmd=="I":
            dq.insert(num,idx)
        else: #cmd=="D"
            dq.delete(num)
    #dq.debug()
    dq.print()
