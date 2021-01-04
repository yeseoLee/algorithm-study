import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
dp=[0 for i in range(n)]

for i in range(n):
    if(i==0):
        dp[i]=a[i]
    elif(i==n-1):
        dp[i]=max(a[i],dp[i-1]+a[i])
    else:
        dp[i]=a[i]+max(dp[i-1],dp[i])

print(max(dp))

'''
평범한 dp
순서가 있는 문제
'''
