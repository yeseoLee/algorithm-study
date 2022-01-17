import sys
n,k=map(int,sys.stdin.readline().split())
w,v=[0],[0]
for i in range(n):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)
dp=[[0 for col in range(k+1)]for row in range(n+1)]


for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
