# BOJ 13913
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
INF = 100001
dp = [INF]*100001
dp[n] = 0
trace = []

que = deque()
que.append(n)
while(que):
    now = que.popleft()
    if now == k:
        break
    if now*2 <= INF and dp[now]+1 < dp[now*2]:
        dp[now*2] = dp[now]+1
        que.append(now*2)
    if now+1 < INF and dp[now]+1 < dp[now+1]:
        dp[now+1] = dp[now]+1
        que.append(now+1)
    if now > 0 and dp[now]+1 < dp[now-1]:
        dp[now-1] = dp[now]+1
        que.append(now-1)

now = k
while(1):
    trace.append(now)
    if now == n:
        break
    if now-1 >= 0 and dp[now-1] == dp[now]-1:
        now -= 1
    elif now+1 < INF and dp[now+1] == dp[now]-1:
        now += 1
    elif now % 2 == 0 and dp[now//2] == dp[now]-1:
        now //= 2

print(dp[k])
print(*trace[::-1])
