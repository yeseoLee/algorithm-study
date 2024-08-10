# 실버 3 N과 M (5) https://www.acmicpc.net/problem/15654

from itertools import permutations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in permutations(arr, m):
    print(*i)
