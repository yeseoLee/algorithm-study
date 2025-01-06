import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

size = [0] * (n + 1)


def count_subtree_nodes(cur_node):
    size[cur_node] = 1
    for nxt_node in graph[cur_node]:
        if size[nxt_node] != 0:
            continue
        size[cur_node] += count_subtree_nodes(nxt_node)
    return size[cur_node]


count_subtree_nodes(r)

for _ in range(q):
    u = int(input())
    print(size[u])
