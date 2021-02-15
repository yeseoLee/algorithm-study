import sys

def DFS(v):
    visited[v]=True
    for i in range(n+1):
        if(graph[v][i]==1 and visited[i]==False):
            DFS(i)

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[0 for i in range(n+1)] for j in range(n+1)]
visited=[False]*(n+1)
count=0

for i in range(m):
    v1,v2=map(int,sys.stdin.readline().split())
    graph[v1][v2]=1
    graph[v2][v1]=1

DFS(1)
print(sum(visited)-1)
