import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graphs = [[] for _ in range(V + 1)]

for _ in range(V):
    li = list(map(int, input().split()))
    for i in range(1, len(li) - 2, 2):
        graphs[li[0]].append((li[i], li[i + 1]))

visited = [False] * (V + 1)
far_v, max_d = 0, 0


def dfs(v, d):
    global far_v, max_d
    if max_d < d:
        max_d = d
        far_v = v

    visited[v] = True
    for nxt_v, nxt_d in graphs[v]:
        if not visited[nxt_v]:
            dfs(nxt_v, d + nxt_d)


dfs(1, 0)
visited = [False] * (V + 1)
dfs(far_v, 0)

print(max_d)
