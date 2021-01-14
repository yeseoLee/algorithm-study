import sys
from collections import deque

n=int(sys.stdin.readline())
dq=deque([x for x in range(1,n+1)])

i=0
while(True):
    if(len(dq)==1):
        print(dq[0])
        break
    if(i%2==0):        
        dq.popleft()
    else:
        dq.append(dq.popleft())
    i+=1
    
