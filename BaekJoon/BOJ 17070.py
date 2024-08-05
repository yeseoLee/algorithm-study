# 골드 5 파이프 옮기기 1 https://www.acmicpc.net/problem/17070

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [[[0 for i in range(3)] for j in range(n)] for k in range(n)]
dp[0][1][0] = 1  # 0: 가로, 1:대각선, 2:세로
for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]

# DP 수행
for i in range(1, n):
    for j in range(1, n):
        # 대각선
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp[i][j][1] = (
                dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
            )  # from 가로,대각선,세로
        # 가로, 세로
        if arr[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]  # from 가로, 대각선
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]  # from 대각선, 세로


print(sum(dp[n - 1][n - 1]))
