#BOJ 11659
import sys
input = sys.stdin.readline

n,m= map(int,input().split())
seq = list(map(int,input().split())) # len: n
arr = [list(map(int,input().split())) for _ in range(m)] # i,j * m

dp=seq[:]
for i in range(1,n):
    dp[i] += dp[i-1]

for i,j in arr:
    print(dp[j-1]-dp[i-1]+seq[i-1])
