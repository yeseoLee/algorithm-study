'''
import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)] # n*n
di,dj=[0,0,1,-1],[1,-1,0,0]

def bfs(x,y):
    que=deque([[x,y,1]])
    while(que):
        i,j,k=que.popleft()
        for a in range(4):
            ni,nj=i+di[a],j+dj[a]
            if 0<= ni<n and 0<=nj<n:
                if arr[ni][nj]==3:
                    return k
                else:
                    que.append([ni,nj,k+1])

def get_chicken_distance(chosen):
    d=0
    for x in chosen:
        i,j=chicken[x][0],chicken[x][1]
        arr[i][j]=3
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                d+=bfs(i,j)
    distance.append(d)
    for x in chosen:
        i,j=chicken[x][0],chicken[x][1]
        arr[i][j]=2
    
def get_m_chicken(chosen:list, used:list,m:int):
    if len(chosen)==m:
        get_chicken_distance(chosen)
        return
    
    start=chosen[-1]+1 if chosen else 0
    for nxt in range(start,len(chicken)):
        if not used[nxt]:
            chosen.append(nxt)
            used[nxt]=True
            get_m_chicken(chosen,used,m)
            chosen.pop()
            used[nxt]=False

# 치킨집 기준으로 백트래킹+그래프
distance=[]
chosen=[]
used=[False]*(13)
chicken=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append([i,j])

get_m_chicken(chosen,used,m)
print(min(distance))
'''
from itertools import combinations 
import sys
input=sys.stdin.readline
n,m=map(int,input().split()) #N*N, 치킨집 M개

#0:빈칸, 1:집 , 2:치킨집
arr=[list(map(int,input().split())) for _ in range(n)]

#치킨거리의 합을 최소로 하는 치킨집 M개
chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            house.append([i,j])
        if arr[i][j]==2:
            chicken.append([i,j])

result=list(combinations(chicken,m))
min_d=float('inf')
for i in range(len(result)): #가능한 모든 조합에 대해
    d=0
    for a,b in house:
        temp=float('inf')
        for j in range(m): #각 조합 안에 있는 원소 수 m개
            temp=min(temp, abs(a-result[i][j][0])+abs(b-result[i][j][1]))
        d+=temp
    min_d=min(min_d,d)
print(min_d)
            
