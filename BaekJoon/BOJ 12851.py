# BOJ 12851 숨바꼭질 2

'''1. 횟수
n에서 시작하여 0~M 까지 가는 최단거리 구하기 (DP)
DP[n][k] = min(DP[n][k-1],DP[n][k+1],DP[n][k//2]) + 1
 
DP2 최단거리로 가는 방법 수
if DP[n][k-1] == DP[n][k] - 1:
DP2[n][k] += DP2[n][k-1]
if DP[n][k+1] == DP[n][k] -1:
DP2[n][k] += DP2[n][k+1] 
if DP2[n][k//2] == DP2[n][k] -1:
DP2[n][k] += DP2[n][k//2]
execption: 유일한가? (겹치는 경우.)  
'''

from collections import deque

MIN, MAX = 0, 100000
n,k = map(int,input().split())

# time
dp=[float('inf')] * (MAX+1)
dp[n] = 0
# way
dp2=[0] * (MAX+1)
dp2[n] = 1

que = deque([n])
while que:
    x = que.popleft()
    if x-1>=MIN and dp[x-1] > dp[x] + 1:
        dp[x-1] = dp[x] + 1
        que.append(x-1)
    if x+1 <= MAX and dp[x+1] > dp[x] + 1:
        dp[x+1] = dp[x] + 1
        que.append(x+1)
    if x*2 <= MAX and dp[x*2] > dp[x] + 1:
        dp[x*2] = dp[x] + 1
        que.append(x*2)

que = deque([n])
visited = [False]*(MAX+1)
while que:
    x = que.popleft()
    if visited[x]:
        continue
    else:
        visited[x] = True
    if x-1>=MIN and dp[x-1] == dp[x] + 1:
        dp2[x-1] += dp2[x]
        que.append(x-1)
    if x+1 <= MAX and dp[x+1] == dp[x] + 1:
        dp2[x+1] += dp2[x]
        que.append(x+1)
    if x*2 <= MAX and dp[x*2] == dp[x] + 1:
        dp2[x*2] += dp2[x]
        que.append(x*2)

#print(dp, dp2)
print(dp[k],dp2[k])