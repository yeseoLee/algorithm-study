n=int(input())

dp=[0]*31
dp[2]=3

for i in range(4, N+1, 2):
    #dp[2]=3가지이고, dp[4],dp[6],dp[8]...에서 나눌 수 없는 모양은 2가지이다
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
print(dp[n])
