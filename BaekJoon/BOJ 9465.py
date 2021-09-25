import sys
input = sys.stdin.readline
t=int(input())

for i in range(t):
    n=int(input())
    arr=[]
    for k in range(2):
        arr.append(list(map(int,input().split())))
    dp=[[0 for x in range(n)] for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n>1:
        dp[0][1] = dp[1][0] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]

    for j in range(2,n):
        dp[0][j] = arr[0][j] + max(dp[1][j-1], dp[1][j-2])
        dp[1][j] = arr[1][j] + max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][n-1],dp[1][n-1]))
