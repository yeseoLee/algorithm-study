'''
import sys
from collections import deque,defaultdict
input=sys.stdin.readline

v,e = map(int,input().split())
k = int(input())

weight=defaultdict(int)
graph=[[] for _ in range(v+1)]

for i in range(e):
    v1,v2,w=map(int,input().split())
    if weight[(v1,v2)]:
        weight[(v1,v2)]=min(weight[(v1,v2)],w)
    else: 
        weight[(v1,v2)]=w
        graph[v1].append(v2)
        
visited=[-1]*(v+1)
visited[k]=0

#DFS (Memory Limit Exceeded)
def dfs(now):
    for next in graph[now]:
        if visited[next]== -1: visited[next]= weight[(now,next)] + visited[now]
        else: visited[next] = min(weight[(now, next)] + visited[now],visited[next])
        dfs(next)
dfs(k)

#BFS (Time Out)
que=deque([k])
while(que):
    now=que.popleft()
    for next in graph[now]:
        #방문 안한 정점
        if visited[next] == -1:
            que.append(next)
            visited[next]= weight[(now,next)] + visited[now]
        #방문 했는데 최단경로가 갱신된 정점
        elif visited[next] > weight[(now, next)] + visited[now]:
            que.append(next)
            visited[next] = weight[(now, next)] + visited[now]

for i in range(1,v+1):
    if visited[i]==-1: print("INF")
    else: print(visited[i])
'''

import sys
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []
def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0,start]) # heap -> [weight,vertex]
    while heap:
        now_w, now_v = heappop(heap)
        for next_v, next_w in s[now_v]:
            next_w += now_w
            #최단 경로 갱신 후 다시 heap에 삽입
            if next_w < dp[next_v]:
                dp[next_v] = next_w
                heappush(heap, [next_w, next_v])
for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
dijkstra(k)
for i in dp[1:]:
    print(i if i != inf else "INF")