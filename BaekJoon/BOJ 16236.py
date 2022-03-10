import sys
from collections import deque

# input & init
input = sys.stdin.readline
n=int(input())
arr = []
shark = [2,0,-9] #shark_size,eat_shark_cnt,sum_shark
for i in range(n):
    arr.append(list(map(int,input().split())))
    shark[2]+=sum(arr[i])
di,dj=[-1,0,0,+1],[0,-1,+1,0] # U,L,R,D

def call_mom(time):
    print(time)

def eat_shark(fish_size):
    shark[2] -= fish_size
    shark[1] += 1
    if shark[0] == shark[1]:
        shark[0]+=1
        shark[1]=0
        
def bfs(i,j,t):
    visited=[[False for a in range(n)] for b in range(n)]
    que =deque([])
    que.append([i,j,t])
    #visited[i][j]=True
    flag=0
    while(que):
        now_i, now_j, time = que.popleft()
        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]
            if not (0<=next_i<n and 0<=next_j<n):
                continue
            elif arr[next_i][next_j] > shark[0]:
                continue
            elif 0 < arr[next_i][next_j] <shark[0]:
                eat_shark(arr[next_i][next_j])
                print(next_i,next_j)
                arr[next_i][next_j]=0
                time += 1
                flag = 1
                break
            elif not visited[next_i][next_j]:
                visited[next_i][next_j]=True
                que.append([next_i,next_j,time+1])
    if(flag):
        if shark[2]==0:
            call_mom(time)
        print(next_i,next_j)
        bfs(next_i,next_j,time)
        return
    call_mom(t)

for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            arr[i][j]=0
            bfs(i,j,0)
            break
