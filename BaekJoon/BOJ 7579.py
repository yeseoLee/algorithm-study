import sys
input=sys.stdin.readline
n,m=map(int,input().split()) #N: number of apps, M: Required memory
memory=list(map(int,input().split()))
cost=list(map(int,input().split()))

dp=[0]*(10000+1) #index=cost,value=memory
dp[0]=0
for i in range(n):
    for j in range(len(dp)-1,-1,-1):
        if j+cost[i] <len(dp):
            dp[j+cost[i]]=max(dp[j+cost[i]],dp[j]+memory[i])

for idx,val in enumerate(dp):
    if val>=m:
        print(idx)
        break
