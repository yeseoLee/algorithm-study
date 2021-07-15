import sys
input=sys.stdin.readline
dx,dy=[0,0,-1,+1],[-1,+1,0,0]

def dfs(x,y):
    if(x==m-1 and y==n-1):
        return 1
    if(dp[x][y]==-1):
        dp[x][y]=0
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if(0<=nx<m and 0<=ny<n):
                if(arr[x][y]>arr[nx][ny]):
                    dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

m,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
dp=[[-1]*n for _ in range(m)]
print(dfs(0,0))

'''
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]
dx,dy=[0,0,-1,+1],[-1,+1,0,0]
cnt=0

def dfs(x,y):
    global cnt
    if(x==m-1 and y==n-1):
        cnt+=1
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if(0<=nx<m and 0<=ny<n):
            if(arr[x][y]>arr[nx][ny] and visited[nx][ny]==False):
                visited[nx][ny]=True
                dfs(nx,ny)
                visited[nx][ny]=False

dfs(0,0)
print(cnt)
'''
