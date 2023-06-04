import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            pass
        elif i==0:
            arr[i][j]+=arr[i][j-1]
        elif j==0:
            arr[i][j]+=arr[i-1][j]
        else:
            arr[i][j]+=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    if(x1==1 and y1==1):
        result=arr[x2-1][y2-1]
    elif(y1==1):
        result=arr[x2-1][y2-1]-arr[x1-2][y2-1]
    elif(x1==1):
        result=arr[x2-1][y2-1]-arr[x2-1][y1-2]
    else:
        result=arr[x2-1][y2-1]-arr[x2-1][y1-2]-arr[x1-2][y2-1]+arr[x1-2][y1-2]
    print(result)

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
s = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]

for i in dp:
    print(i)
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))
'''
