import sys
inf=100000000
def solve(s,e):
    if(e-s==1):
        dp[s][e]=sum(ch[s:e+1])
        return
    min_cost=inf
    for bd in range(s,e):
        if(s!=bd and dp[s][bd]==0):
            solve(s,bd)
        if((bd+1)!=e and dp[bd+1][e]==0):
            solve(bd+1,e)
        cost=dp[s][bd]+dp[bd+1][e]+sum(ch[s:e+1])
        if(min_cost>cost):
            min_cost=cost
    dp[s][e]=min_cost
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    ch=list(map(int,sys.stdin.readline().split()))
    dp=[[0 for i in range(k+1)] for j in range(k+1)]
    solve(0,k)
    print(dp[0][k-1])
