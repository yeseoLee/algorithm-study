def bfs(tx,ty):
    while(que):
        x,y=que.popleft()
        v=visited[x][y]
        if(x==tx and y==ty):
            return v
        for i in range(8):
            xx=x+dx[i]
            yy=y+dy[i]
            if(0<=xx<=l-1 and 0<=yy<=l-1 and visited[xx][yy]==0):
                que.append([xx,yy])
                visited[xx][yy]=v+1
        
from collections import deque
import sys
t=int(sys.stdin.readline())

for i in range(t):
    l=int(sys.stdin.readline())
    fx,fy=map(int,sys.stdin.readline().split()) #from
    tx,ty=map(int,sys.stdin.readline().split()) #to
    visited=[[0 for x in range(l)] for y in range(l)]
    dx=[1,1,2,2,-1,-1,-2,-2]
    dy=[2,-2,1,-1,2,-2,1,-1]
    que=deque([[fx,fy]])
    visited[fx][fy]=1
    print(bfs(tx,ty)-1)
