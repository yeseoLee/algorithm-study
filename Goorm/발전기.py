import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]


def bfs(i, j):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            bfs(i, j)

print(cnt)
