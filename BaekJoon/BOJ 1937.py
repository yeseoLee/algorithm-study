# BOJ 1937
sys.setrecursionlimit(10**8)
import sys
# input
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# init
dp = [[1 for col in range(n)] for row in range(n)]
visited = [[False for col in range(n)] for row in range(n)]
di, dj = [0, 0, +1, -1], [+1, -1, 0, 0]

# logic
def dfs(i, j):
    visited[i][j] = True
    for a in range(4):
        ni, nj = i+di[a], j+dj[a]
        if 0 <= ni < n and 0 <= nj < n and arr[i][j] < arr[ni][nj]:
            if not visited[ni][nj]:
                dfs(ni, nj)
            dp[i][j] = max(dp[i][j], dp[ni][nj]+1)
max_move = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
        max_move = max(max_move, dp[i][j])

# output
print(max_move)
