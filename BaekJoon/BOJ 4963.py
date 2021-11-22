import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_island(zido: list, w:int ,h:int) -> int :
    visited=[[False for col in range(w)] for row in range(h)]
    dx,dy=[0,0,+1,-1,+1,+1,-1,-1],[+1,-1,0,0,+1,-1,+1,-1]
    cnt=0
    
    def dfs(x,y):
        visited[x][y]=True
        for i in range(8):
            if 0<=x+dx[i]<h and 0<=y+dy[i]<w:
                if not visited[x+dx[i]][y+dy[i]] and zido[x+dx[i]][y+dy[i]]==1:
                    dfs(x+dx[i],y+dy[i])

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and zido[i][j]==1:
                dfs(i,j)
                cnt+=1        
    return cnt

while(1):
    w,h=map(int,input().split())
    if w==h==0: break
    zido=[]
    for i in range(h):
        zido.append(list(map(int,input().split())))
    print(get_island(zido,w,h))
