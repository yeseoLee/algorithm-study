import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
year=0
dx,dy=[0,0,+1,-1],[+1,-1,0,0]

def get_ice():
    def _adj_sea(x,y):
        sea_count=0
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not arr[nx][ny] and not visited[nx][ny]:
                sea_count+=1
        return sea_count

    def _bfs(x,y):
        visited[x][y]=1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 1<=nx<n-1 and 1<=ny<m-1:
                if arr[nx][ny] and not visited[nx][ny]:
                    arr[nx][ny]=arr[nx][ny]-_adj_sea(nx,ny) if arr[nx][ny]>_adj_sea(nx,ny) else 0 #melt
                    _bfs(nx,ny)
    ice=0
    visited=[[0 for col in range(m)] for row in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j] and not visited[i][j]:
                ice+=1
                if ice>1:
                    return ice
                arr[i][j]=arr[i][j]-_adj_sea(i,j) if arr[i][j]>_adj_sea(i,j) else 0 #melt
                _bfs(i,j)
    return ice

while(True):
    year+=1
    ice=get_ice()
    if ice==0:
        print(0)
        break
    elif ice==2:
        print(year-1)
        break
