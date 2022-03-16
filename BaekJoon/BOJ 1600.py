import sys
from collections import deque
input = sys.stdin.readline

def dfs(i,j,k):
    arr[i][j]=k # init
    count[i][j]=0
    que=deque([])
    que.append([i,j])
    while(que):
        x,y = que.popleft() #x,y -> coordinate
        cnt=count[x][y]
        z=arr[x][y]
        #monkey-move
        for a in range(4):
            nx,ny=x+mx[a],y+my[a]
            if (0<=nx<h and 0<=ny<w and arr[nx][ny]!=z):
                if (arr[nx][ny]==-1):
                    continue
                arr[nx][ny]=z
                count[nx][ny]=min(count[nx][ny],cnt+1)
                que.append([nx,ny])
        if z==0:
            continue
        #horse-move
        for a in range(8):
            nx,ny = x+hx[a],y+hy[a]
            if (0<=nx<h and 0<=ny<w and arr[nx][ny]!=z-1):
                if (arr[nx][ny]==-1):
                    continue
                arr[nx][ny]=z-1
                count[nx][ny]=min(count[nx][ny],cnt+1)
                que.append([nx,ny])

k=int(input())
w,h = map(int,input().split())
arr=[list(map(lambda x: -1 if x==1 else k+1, map(int,input().split()))) for _ in range(h)]

mx,my = [+1, -1, 0, 0],[0,0,+1,-1]
hx,hy = [+2,+2,+1,+1,-2,-2,-1,-1],[+1,-1,+2,-2,+1,-1,+2,-2]
inf=40001
count = [[inf for col in range(w)] for row in range(h)]

dfs(0,0,k)
if count[w-1][h-1]==inf:
    print(-1)
else:
    print(count[w-1][h-1])
