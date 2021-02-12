import sys
n=int(sys.stdin.readline())
a=[]
dp=[1 for i in range(n)]
a=list(map(int,sys.stdin.readline().split()))
for i in range(1,n):
    for j in range(i):
        if(a[i]>a[j]):
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
