import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

p = [v for v in range(0, n + 1)]


# 해당 원소의 집합 찾기
def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]


# 두 집합 결합
def union_p(p, a, b):
    a = find_p(p, a)
    b = find_p(p, b)
    if a == b:
        return False
    elif a < b:
        p[b] = a
    else:
        p[a] = b
    return True


result = 0
for edge in edges:
    c, a, b = edge

    if union_p(p, a, b):
        result += c

print(result)
