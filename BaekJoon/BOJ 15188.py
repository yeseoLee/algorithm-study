# 실버 2 1, 2, 3 더하기 3

MAX_N = 1000000
MAX_CNT = 1000000009

dp = [1] * (MAX_N + 1)
dp[2] = 2
for i in range(3, MAX_N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MAX_CNT


t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
