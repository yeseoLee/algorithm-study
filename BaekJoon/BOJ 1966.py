import sys
from collections import deque

t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    priority=list(map(int,sys.stdin.readline().split()))
    dq=deque()
    for a,b in enumerate(priority):
        dq.append((a,b)) #a:인덱스,b:우선순위
    rank=1
    while(True):
        first=dq[0]
        for j in dq:
            if(j[1]>first[1]):
                dq.append(dq.popleft())
                break
        else:
            if(dq.popleft()[0]==m):
                print(rank)
                break
            rank+=1
