from collections import deque
import sys
input=sys.stdin.readline

def bfs(x):
    q=deque([x])
    visited=[False]*(n+1)
    visited[x]=True
    cnt=1
    while q:
        nxt=q.popleft()
        for i in graph[nxt]:
            if not visited[i]:
                visited[i] = True 
                cnt+=1
                q.append(i)
    return cnt

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

count=[0]*(n+1)
for i in range(1,n+1):
    count[i] = bfs(i)

print(*[idx for idx,val in enumerate(count) if val==max(count)])
