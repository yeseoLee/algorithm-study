from collections import deque
def bfs():
    que=deque([[0,0,1]])
    while(que):
        x,y,cnt=que.popleft()
        print(f"x:{x},y:{y},cnt:{cnt}")
        #(N,M)에 도착
        if(x==m-1 and y==n-1):
            print(cnt)
            return -1
        for dx,dy in zip(pmx,pmy):
            curX,curY=x+dx,y+dy
            #out of range
            if(curX<0 or curX>=m or curY<0 or curY >=n):
                continue        
            #탐색 가능한 길을 찾음
            if(arr[curY][curX]==1 and visited[curY][curX]==False):
                que.append([curX,curY,cnt+1])
                visited[curY][curX]=True
 
n,m=map(int,input().split())
arr=[list(map(int,input()))for i in range(n)]
visited=[[False for row in range(m)] for col in range(n)]
pmy=[0,+1,-1,0]
pmx=[+1,0,0,-1]
bfs()
'''
from collections import deque
def dfs(x,y,cnt):
    print(f"x:{x},y:{y},cnt:{cnt}")
    #(N,M)에 도착
    if(x==m-1 and y==n-1):
        way.append(cnt)    
    visited[y][x]=True
    for dx,dy in zip(pmx,pmy):
        curX,curY=x+dx,y+dy
        #out of range
        if(curX<0 or curX>=m or curY<0 or curY >=n):
            continue        
        #탐색 가능한 길을 찾음
        if(arr[curY][curX]==1 and visited[curY][curX]==False):
            dfs(curX,curY,cnt+1)      
        
n,m=map(int,input().split())
arr=[list(map(int,input()))for i in range(n)]
visited=[[False for row in range(m)] for col in range(n)]
pmy=[0,+1,-1,0]
pmx=[+1,0,0,-1]
way=[]

dfs(0,0,1)
print(min(way))
'''


