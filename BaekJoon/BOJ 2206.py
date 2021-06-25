'''
def dfs(x,y,cnt,b):
    global min_cnt
    if(x==n-1 and y==m-1):
        if(min_cnt<0): min_cnt=cnt
        else: min_cnt=min(min_cnt,cnt)
        return -1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<m and visited[nx][ny]==False):
            if(arr[nx][ny]=='0'):
                visited[nx][ny]=True
                dfs(nx,ny,cnt+1,b)
                visited[nx][ny]=False
            else:
                if(b==1):
                    visited[nx][ny]=True
                    dfs(nx,ny,cnt+1,b-1)
                    visited[nx][ny]=False
        
import sys
n,m=map(int,sys.stdin.readline().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
min_cnt=-1
dfs(0,0,1,1)
print(min_cnt)
'''

from collections import deque
def bfs(x,y,b):
    que=deque([(x,y,b)])
    trace[x][y][b]=1
    while(que):
        x,y,b=que.popleft()
        if(x==n-1 and y==m-1):
            return trace[x][y][b]
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if(0<=nx<n and 0<=ny<m):
                if(arr[nx][ny]=='0' and trace[nx][ny][b]==0):
                    trace[nx][ny][b]=trace[x][y][b]+1
                    que.append((nx,ny,b))
                elif(arr[nx][ny]=='1' and b==1):
                        trace[nx][ny][b-1]=trace[x][y][b]+1
                        que.append((nx,ny,b-1))
    return -1

import sys
n,m=map(int,sys.stdin.readline().split())
arr=[list(sys.stdin.readline()) for _ in range(n)]
trace=[[[0,0] for _ in range(m)] for _ in range(n)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
print(bfs(0,0,1))
