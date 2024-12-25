import sys

input = sys.stdin.readline

n, m = map(int, input().split())

table = {}
for _ in range(n):
    k, v = input().rstrip().split()
    table[k] = v

for _ in range(m):
    k = input().rstrip()
    print(table[k])
