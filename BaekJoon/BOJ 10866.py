import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
line=list(map(int,sys.stdin.readline().split()))
dq=deque([x for x in range(1,n+1)])
cnt=0
for item in line:
    dqc,dqcc=0,0
    dqcopy=dq.copy()
    while(item!=dqcopy[0]):
        dqcopy.append(dqcopy.popleft())
        dqcc+=1
    while(item!=dq[0]):
        dq.appendleft(dq.pop())
        dqc+=1
    if(dqcc<dqc):
        dqcopy.popleft()
        dq=dqcopy
        cnt+=dqcc
    else:
        dq.popleft()
        cnt+=dqc
print(cnt)
            
        

