import sys
v, e = map(int, sys.stdin.readline().split())
inf = 100000000
s = [[inf] * v for i in range(v)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = c
for k in range(v):
    for i in range(v):
        for j in range(v):
            s[i][j] = min(s[i][j],s[i][k] + s[k][j])
result = inf
for i in range(v):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)

'''
import sys
import heapq

inf=400*10002
def dijkstra(x):
    for cost,next in graph[x]:
        heapq.heappush(que,(cost,next))
    while(que):
        now_cost,now = heapq.heappop(que)
        if now==x:
            return now_cost
        if visited[now]:
            continue
        visited[now]=True
        weight[now]=min(weight[now],now_cost)
        for next_cost,next in graph[now]:
            heapq.heappush(que,(now_cost+next_cost,next))
    return -1

input = sys.stdin.readline
v,e = map(int,input().split())
graph=[[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split()) # a->b cost c
    graph[a].append([c,b])


min_cycle=inf
for i in range(1,v+1):
    que = []
    weight=[inf]*(v+1)
    visited=[False]*(v+1)
    now_cycle = dijkstra(i)
    if now_cycle!=-1:
        min_cycle = min(min_cycle,now_cycle)
if min_cycle==inf:
    min_cycle=-1
print(min_cycle)

'''
