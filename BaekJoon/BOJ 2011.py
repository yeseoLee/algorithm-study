import sys
input = sys.stdin.readline
num=list(input().strip())
dp=[0]*(len(num)+1)
dp[0]=dp[1]=1

if num[0] == '0':
    print(0)
else:
    for i in range(2,len(num)+1):
        if int(num[i-1])>0:
            dp[i]+=dp[i-1]
        if 10<= int(num[i-2])*10 + int(num[i-1])<=26:
            dp[i]+=dp[i-2]
    print(dp[len(num)] % 1000000)
