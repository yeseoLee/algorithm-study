# BOJ 10026
from collections import deque
import sys
input = sys.stdin.readline

# input
n = int(input())
paint = [list(input().rstrip()) for _ in range(n)]

# init
blind_count, normal_count = 0, 0
visited = [[False for col in range(n)] for row in range(n)]
dx, dy = [0, 0, +1, -1], [+1, -1, 0, 0]

# logic
def bfs(x, y):
    visited[x][y] = True
    que = deque()
    que.append((x, y))
    while(que):
        x, y = que.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if paint[x][y] == paint[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_count += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'G':
            paint[i][j] = 'R'
visited = [[False for col in range(n)] for row in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            blind_count += 1
            bfs(i, j)

# output
print(normal_count, blind_count)
