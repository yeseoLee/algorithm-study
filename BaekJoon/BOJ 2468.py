import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
max_safe=0
dx,dy=[0,0,+1,-1],[+1,-1,0,0]

for rain in range(0,101):
    safe=0
    #침수
    flooding = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= rain:
                flooding[i][j] = 1
    #완전 탐색     
    for i in range(n):
        for j in range(n):
            if flooding[i][j] == 0: # not 침수
                safe+=1
                #BFS
                que=deque([(i,j)])
                while(que):
                    x,y = que.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and flooding[nx][ny]==0:
                            flooding[nx][ny]=1
                            que.append((nx,ny))
    if safe==0: #전부 침수
        break
    max_safe=max(max_safe,safe)     

print(max_safe)
    
