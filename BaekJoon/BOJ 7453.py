# BOJ 7453 합이 0 인 네 정수 골드 2 https://www.acmicpc.net/problem/7453

import sys

input = sys.stdin.readline
n = int(input())

A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort()
CD.sort()

answer = 0

# 슬라이딩 윈도우
L, R = 0, len(AB) - 1
while L < len(AB) and R > -1:
    s = AB[L] + CD[R]
    if s > 0:
        R -= 1
    elif s < 0:
        L += 1
    else:
        # 동일한 숫자 압축
        x = 1
        for i in range(L + 1, len(AB)):
            if AB[L] == AB[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(R - 1, -1, -1):
            if CD[R] == CD[i]:
                y += 1
            else:
                break
        answer += x * y
        L += x
        R -= y

print(answer)
