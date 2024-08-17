# 골드 5 하노이 탑 https://www.acmicpc.net/problem/1914

import sys

sys.setrecursionlimit(10**6)

n = int(input())


def hanoi(n, s, v, e):
    if n == 1:
        print(s, e)
        return
    hanoi(n - 1, s, e, v)
    print(s, e)
    hanoi(n - 1, v, s, e)


cnt = 0
for i in range(n):
    cnt += 2**i

print(cnt)
if n <= 20:
    hanoi(n, 1, 2, 3)
