# BOJ 24479 실버 2 알고리즘 수업 - 깊이 우선 탐색 1

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()
    graph[i].sort()

visited = [0] * (n + 1)


def dfs(now):
    global cnt
    cnt += 1
    visited[now] = cnt

    for nxt in graph[now]:
        if visited[nxt] == 0:
            dfs(nxt)
    return


cnt = 0
dfs(r)

for i in visited[1:]:
    print(i)
