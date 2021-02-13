import sys
from collections import deque

'''def DFS(graph, v):
    visited=[False] * (n+1)
    s=deque()
    s.appendleft(v)
    while(s):
        if(visited[s[0]]==False):
            print(s[0],end=" ")
            visited[s[0]]=True
            for i in graph[s[0]]:
                if(visited[i]==False):
                    s.appendleft(i)
                    break
        else:
            s.popleft()
    print()
'''
def DFS(v):
    visited[v]= True
    print(v,end=' ')
    for i in graph[v]:
        if(visited[i]==False):
            DFS(i)
def BFS(v):
    visited=[False] * (n+1)
    q=deque()
    q.append(v)
    visited[v]=True
    while(q):
        for i in graph[q[0]]:
            if(visited[i]==False):
                q.append(i)
                visited[i]=True
        print(q.popleft(),end=" ")

#n=정점개수 m=간선개수 v=시작정점 graph=정점과 간선을 저장하는 배열
n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visited=[False] * (n+1)

#두 정점을 잇는 간선 입력
for i in range(m):
    v1,v2=map(int,sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

#작은 순서대로 정렬 (오름차순)
for i in range(n+1):
    graph[i]=sorted(graph[i])

#DFS, BFS 호출
DFS(v)
print()
BFS(v)
