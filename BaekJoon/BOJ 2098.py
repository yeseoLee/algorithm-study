# 골드 1 외판원 순회
# https://www.acmicpc.net/problem/2098

import sys

input = sys.stdin.readline


# input
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# init
MAX_COST = int(1e9)
dp = {}


# logic
def dfs(now, visited):
    # 비트 시프트 연산
    if visited == (1 << n) - 1:
        return w[now][0] if w[now][0] else MAX_COST

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = MAX_COST
    for next in range(1, n):
        # w[i][i]는 항상 0 / 비트 and 연산
        if w[now][next] == 0 or visited & (1 << next):
            continue
        # 비트 or 연산
        cost = dfs(next, visited | (1 << next)) + w[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost


# output

# 어짜피 순환 구조이므로 어느 점에서 시작하던지 결과값은 동일하다
print(dfs(0, 1))
