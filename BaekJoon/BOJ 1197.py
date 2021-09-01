import sys
import heapq
imput=sys.stdin.readline

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
visited=[False]*(v+1)
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


    
    
