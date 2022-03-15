import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx,dy=[+1,-1,0,0],[0,0,+1,-1]

def dfs(i,j):
    visited[i][j]=True
    que=deque([])
    que.append([i,j])
    unite=[]
    sum_unite=0
    while(que):
        x,y = que.popleft()
        unite.append([x,y])
        sum_unite+=arr[x][y]
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                visited[nx][ny]=True
                que.append([nx,ny])
    return [sum_unite,unite]

def move_unite(sum_unite,unite):
    population = sum_unite // len(unite)
    for x,y in unite:
        arr[x][y] = population

move_count=0
while(True):
    visited=[[False for col in range(n)] for row in range(n)]
    flag=1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sum_unite, unite = dfs(i,j)
                if len(unite)!=1:
                    move_unite(sum_unite,unite)
                    flag=0
    if flag:
        break
    move_count+=1
    continue

print(move_count)
