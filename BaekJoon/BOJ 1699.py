from math import sqrt
n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1): # n 이하의 모든 자연수 i에 대해
    s=[]
    for j in range(1,int(sqrt(i))+1): # i보다 작은 제곱수 j에 대해
        s.append(dp[i-j*j]) # dp[i-j]중 가장 작은 값
    dp[i]=min(s)+1
print(dp[n])
