# 실버 1 동물원 https://www.acmicpc.net/problem/1309

import sys

n = int(input())
dp = [[0 for i in range(3)] for j in range(n)]
cnt = 1

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, n):
    dp[i][0] = sum(dp[i - 1]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[-1]) % 9901)
