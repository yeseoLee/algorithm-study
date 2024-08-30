import sys
import heapq

input = sys.stdin.readline

# input & init
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

for g in graph:
    g.sort()

S, E = map(int, input().split())

costs = [float("inf")] * (N + 1)
q = [(0, S, [S])]

# logic
while q:
    cost, now, trace = heapq.heappop(q)
    if now == E:
        print(cost)
        print(len(trace))
        print(*trace)
        break
    for nxt_cost, nxt in graph[now]:
        nxt_cost += cost
        if nxt_cost < costs[nxt]:
            costs[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, nxt, trace + [nxt]))
