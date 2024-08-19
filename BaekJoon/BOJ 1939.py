# 골드 3 중량제한 https://www.acmicpc.net/problem/1939

import sys
import heapq

n, m = map(int, input().split())

graph = [[] for j in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n + 1):
    graph[i].sort(reverse=True)


def dijstra(s, e):
    h = []
    heapq.heappush(h, (0, s))

    while h:
        now_w, now = heapq.heappop(h)
        now_w *= -1

        if now == e:
            return now_w
        if weights[now] > now_w:
            continue

        for nxt_w, nxt in graph[now]:
            w = nxt_w if now_w == 0 else min(nxt_w, now_w)
            if weights[nxt] < w:
                weights[nxt] = w
                heapq.heappush(h, (-w, nxt))


weights = [0] * (n + 1)
s, e = map(int, input().split())
print(dijstra(s, e))
