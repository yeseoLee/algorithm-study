from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int,input().split()) # n: vertex m: edge
graph=[[] for _ in range(n+1)] #graph
cnt=0 #Count of Connected Component

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False]*(n+1)

def bfs(n: int):
    visited[n]=True
    que=deque([n])
    while(que):
        x = que.popleft()
        for next in graph[x]:
            if not visited[next]:
                visited[next]=True
                que.append(next)
    
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt+=1

print(cnt)
    
    
    
