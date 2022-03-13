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
    sys.exit(0)

def eat_shark(fish_size):
    shark[2] -= fish_size
    shark[1] += 1
    if shark[0] == shark[1]:
        shark[0]+=1
        shark[1]=0
def get_next(start,hubo):
    if len(hubo)==1:
        return hubo[0]

    min_weight = [start[0]-hubo[0][0],start[1]-hubo[0][1],0]
    for idx,val in zip(range(len(hubo)),hubo):
        weight = [start[0]-val[0],start[1]-val[1],idx]
        if ( (weight[0]>min_weight[0]) or (weight[0]==min_weight[0] and weight[1]>min_weight[1]) ):
            min_weight=weight
    return hubo[min_weight[2]]


def bfs(i,j,t):
    visited=[[False for a in range(n)] for b in range(n)]
    que =deque([])
    que.append([i,j,t])
    visited[i][j]=True
    flag=0
    hubo=[]
    while(que):
        now_i, now_j, time = que.popleft()
        if flag and hubo[0][2]<=time:
            continue
        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]
            if not (0<=next_i<n and 0<=next_j<n):
                continue
            elif arr[next_i][next_j] > shark[0]:
                continue
            elif 0 < arr[next_i][next_j] <shark[0]:
                hubo.append([next_i,next_j,time+1])
                flag = 1
                break
            elif not visited[next_i][next_j]:
                visited[next_i][next_j]=True
                que.append([next_i,next_j,time+1])
    if flag:
        start=[i,j]
        next_i,next_j,time = get_next(start,hubo)
        eat_shark(arr[next_i][next_j])
        arr[next_i][next_j]=0
        bfs(next_i,next_j,time)
    else:
        call_mom(t)

for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            arr[i][j]=0
            bfs(i,j,0)
            break
