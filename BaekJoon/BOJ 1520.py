'''
import sys
from collections import deque
def bfs(x,y):
    cnt=0
    que=deque([])
    que.append((x,y))
    while(que):
        x,y=que.popleft()
        for dx,dy in [[1,0],[-1,0],[0,1]]:
            if(x+dx<0 or x+dx>=n or y+dy<0 or y+dy>=m):
                continue
            elif(x+dx==n-1 and y+dy==m-1):
                cnt+=1
            elif(arr[y][x]>arr[y+dy][x+dx]):
                que.append((x+dx,y+dy))
    return cnt
    
input=sys.stdin.readline
m,n=map(int,input().split()) #m:세로 n:가로
arr=[list(map(int,input().split())) for _ in range(m)]

print(bfs(0,0))

'''
import sys
from queue import PriorityQueue
input=sys.stdin.readline
m,n=map(int,input().split()) #m:세로 n:가로
arr=[list(map(int,input().split())) for _ in range(m)] #각 칸의 높이
que=PriorityQueue()
cnt=[[0]*n for _ in range(m)]  # 그 칸에 가는 방법 수
cnt[0][0]=1 #시작점 
for y in range(m):
    for x in range(n):
        que.put((-arr[y][x],(y,x))) #우선순위 큐에 넣고 큰 수부터 뽑아서 연산
    for x in range(n):
        i,j=que.get()[1]
        if(j>0 and  arr[i][j-1]>arr[i][j]):
            cnt[i][j]+=cnt[i][j-1]
        if(j<n-1 and arr[i][j+1]>arr[i][j]):
            cnt[i][j]+=cnt[i][j+1]
        if(i>0 and arr[i-1][j]>arr[i][j]):
            cnt[i][j]+=cnt[i-1][j]
        if(i<m-1 and arr[i+1][j]>arr[i][j]):
            cnt[i][j]+=cnt[i+1][j]
print(cnt[m-1][n-1])
            
        
