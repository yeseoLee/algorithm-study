import sys
n,k=map(int,sys.stdin.readline().split())
a=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
dp=[0 for i in range(k+1)]


for i in range(n):
    for j in range(k, 1, -1):
        if(a[i][0] <= j):
            dp[j]=max(dp[j],dp[j-a[i][0]] +a[i][1])

print(dp[-1])
"""
못푼문제
방향을 이상하게 잡았음
"""


                
