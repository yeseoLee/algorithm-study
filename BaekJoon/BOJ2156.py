import sys

n=int(sys.stdin.readline())
podo=[0 for i in range(10000)]
dp=[0 for i in range(10000)]
for i in range(n):
    podo[i]=int(sys.stdin.readline())

dp[0]=podo[0]
dp[1]=podo[0]+podo[1]
dp[2]=max(dp[1],podo[0]+podo[2],podo[1]+podo[2])

for i in range(3,n):
    a=podo[i]+podo[i-1]+dp[i-3]
    b=podo[i]+dp[i-2]
    c=podo[i-1]+podo[i-2]+dp[i-4]
    dp[i]=max(a,b,c)
print(max(dp[n-1],dp[n-2]))

"""
바로 직전 원소를 더할때
dp[i]=podo[i]+podo[i-1]+dp[i-3]
그렇지 않을 때
dp[i]=podo[i]+dp[i-2]
자기 자신 미포함
dp[i]=podo[i-1]+podo[i-2]+dp[i-4]
"""
