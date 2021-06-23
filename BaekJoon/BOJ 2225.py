'''0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수'''
n,k=map(int,input().split())
dp=[[0]*(n+1) for _ in range(k+1)]
for i in range(1,k+1):
    dp[i][1]=i
for i in range(1,k+1):
    for j in range(2,n+1):
        if(i==1):
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i][j-1]+dp[i-1][j])%1000000000
print(dp[k][n])
'''
0+(n,k-1)
1+(n-1,k-1)
2+(n-2,k-1)
n-1+(1,k-1)
n+(0,k-1) 

n,1 = 1개
n,2 = n+1개

   1 2 3
1 1 2 3
2 1 3 6
3 1 4 10
4 1 5 15
'''
