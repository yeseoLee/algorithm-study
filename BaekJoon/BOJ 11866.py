import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

d1=deque([x for x in range(1,n+1)])
d2=deque()
result=[]
i=1
while(i<=n*k):
    if(i%k==0):
        result.append(d1.popleft())
    else:
        d2.append(d1.popleft())
    if(len(d1)==0):
        d1,d2=d2,d1
    i+=1

print("<",end="")
for a,b in enumerate(result):
    if(a!=len(result)-1):
        print(b,end=", ")
    else:
        print(b,end=">")
        
