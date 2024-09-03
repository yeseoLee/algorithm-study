import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())

graphs = []
for _ in range(E):
    s, e, c = map(int, input().split())
    graphs.append((s, e, c))

graphs.sort(key=lambda x: x[2])

parent = [x for x in range(V + 1)]


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


result = 0
for s, e, c in graphs:
    if find(s) != find(e):
        union(s, e)
        result += c

print(result)
