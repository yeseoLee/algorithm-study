# BOJ 1238 골드 3 https://www.acmicpc.net/problem/1238

import sys
import heapq

input = sys.stdin.readline


N, M, X = map(int, input().split())
X -= 1

graph = [[] for j in range(N)]
for i in range(M):
    s, e, t = map(int, input().split())
    graph[s - 1].append((e - 1, t))

""" 2656ms 시간 풀이 (아래는 980ms 풀이)  
def bfs(s, e):
    distance = [-1] * N
    heap = []
    heapq.heappush(heap, (0, s))

    while heap:
        now_d, now = heapq.heappop(heap)
        for nxt, nxt_d in graph[now]:
            if nxt_d == -1:
                continue

            dist = now_d + nxt_d
            if distance[nxt] == -1 or distance[nxt] > dist:
                distance[nxt] = dist
                heapq.heappush(heap, (dist, nxt))

    return distance[e]


costs_from_X = [0] * N
costs_to_X = [0] * N
for i in range(N):
    if i == X:
        continue
    costs_from_X[i] = bfs(X, i)
    costs_to_X[i] = bfs(i, X)
"""


def bfs(s):
    distance = [-1] * N
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0

    while heap:
        now_d, now = heapq.heappop(heap)
        if distance[now] < now_d:
            continue

        for nxt, nxt_d in graph[now]:
            dist = now_d + nxt_d
            if distance[nxt] == -1 or distance[nxt] > dist:
                distance[nxt] = dist
                heapq.heappush(heap, (dist, nxt))

    return distance


costs_from_X = bfs(X)
costs_to_X = [bfs(i)[X] for i in range(N)]

costs = [x + y for x, y in zip(costs_to_X, costs_from_X)]

print(max(costs))
