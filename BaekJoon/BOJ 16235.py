import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
a = [[5 for col in range(n)] for row in range(n)]
tree=[[deque() for col in range(n)] for row in range(n)]
ans=0
for i in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)
    ans+=1
dx,dy=[0,0,+1,+1,+1,-1,-1,-1],[+1,-1,0,+1,-1,0,+1,-1]

def year():
    global ans
    breeding=[]
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for t in range(len(tree[i][j])):  # 봄 성장
                    if a[i][j]>=tree[i][j][t]:
                        a[i][j]-=tree[i][j][t]
                        tree[i][j][t]+=1
                        #가을 번식 추가
                        if tree[i][j][t]%5==0:
                            breeding.append((i, j))
                    else:
                        while t < len(tree[i][j]):
                            a[i][j] += (tree[i][j].pop()//2)
                            ans -=1
                        break
            #겨울 양분 추가
            a[i][j]+=A[i][j]
    #가을 번식
    for x,y in breeding:
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                tree[nx][ny].appendleft(1)
                ans+=1

def count_trees():
    result=0
    for i in range(n):
        for j in range(n):
            result+=len(tree[i][j])
    return result

for i in range(k):
    year()
print(count_trees())