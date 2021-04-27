from collections import deque
import sys
m,n,h=map(int,sys.stdin.readline().split())
arr=[[list(map(int,sys.stdin.readline().split())) for i in range(n)] for j in range(h)]
#익힘을 전달하는 방향
dx=[+1,-1,0,0,0,0]
dy=[0,0,+1,-1,0,0]
dz=[0,0,0,0,+1,-1]
# 익은 토마토는 주변 탐색을 위해 큐에 넣는다.
que=deque([])
for i in range(n):
    for j in range(m):
        for k in range(h):
            if(arr[k][i][j]==1):
                que.append([k,i,j])
#BFS
while(que):
    k,i,j=que.popleft()
    for di,dj,dk in zip(dx,dy,dz):
        #MxNxH 범위 내에서
        if(-1< (i+di) < n and -1<(j+dj) < m and -1<(k+dk) < h
        and arr[k+dk][i+di][j+dj]==0):
            que.append([k+dk,i+di,j+dj])
            arr[k+dk][i+di][j+dj]=arr[k][i][j]+1
# 익지 않은 토마토가 있는지
z=1
day=-1
for i in arr:
    for j in i:
        for k in j:
            if k==0:
                z=0
            day=max(day,k)
if(z==0):
    print(-1)
elif(day==1):
    print(0)
else:
    print(day-1)

'''3차원 배열은 [layer][row][colunm] 순이다.'''
