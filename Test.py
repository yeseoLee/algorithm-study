from collections import deque
import sys
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for row in range(n)]
day=-1
que=deque([])
que2=[]
di=[1,-1,0,0]
dj=[0,0,1,-1]

for i in range(n):
    for j in range(m):
        if(arr[i][j]==1):
            que.append([i,j])

while(que):
    while(que):
        ti,tj=que.popleft()
        for i,j in zip(di,dj):
            try:
                if(ti+i>-1 and tj+j>-1 and arr[ti+i][tj+j]==0):
                    arr[ti+i][tj+j]=1
                    que2.append([ti+i,tj+j])
            except: 
                pass
    que=deque(que2)
    que2=[]
    day+=1

for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            print(-1)
            sys.exit()
print(day)
