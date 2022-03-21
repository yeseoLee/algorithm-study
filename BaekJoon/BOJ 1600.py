import sys
from collections import deque
input = sys.stdin.readline

def dfs(i,j,k):
    que=deque()
    que.append((i,j,k))
    visited = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
    while(que):
        x,y,z= que.popleft() #x,y -> coordinate
        if (x==h-1 and y==w-1):
            return visited[x][y][z]
        #monkey-move
        for a in range(4):
            nx,ny=x+mx[a],y+my[a]
            if(0<=nx<h and 0<=ny<w and arr[nx][ny]!=1 and visited[nx][ny][z]==0):
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append((nx,ny,z))
        if z==0:
            continue
        #horse-move
        for a in range(8):
            nx,ny = x+hx[a],y+hy[a]
            if(0<=nx<h and 0<=ny<w and arr[nx][ny]!=1 and visited[nx][ny][z-1]==0):
                visited[nx][ny][z-1] = visited[x][y][z] + 1
                que.append((nx,ny,z-1))
    return -1

k=int(input())
w,h = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(h)]

mx,my = [+1, -1, 0, 0],[0,0,+1,-1]
hx,hy = [+2,+2,+1,+1,-2,-2,-1,-1],[+1,-1,+2,-2,+1,-1,+2,-2]
inf=40001

print(dfs(0,0,k))
