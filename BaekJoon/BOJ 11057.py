import sys
input = sys.stdin.readline
n=int(input())

dp = [[1 for col in range(10)] for row in range(1001)]

for i in range(1,1001): # cipher
    for j in range(1,10): # max_value
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(dp[n][9])


''' recursive -> (X)
sys.setrecursionlimit(10**8)
def ascending(min_value,cipher):
    if cipher==1:
        return 10-min_value
    result=0
    for i in range(min_value,10):
        result+=ascending(i,cipher-1)
    return result%10007

print(ascending(0,n))
'''
