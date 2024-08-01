# 골드 4 알고스팟 https://www.acmicpc.net/problem/1261

import sys
import heapq


input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

result = 0
dx, dy = [0, 0, +1, -1], [+1, -1, 0, 0]
visited = [[False for i in range(m)] for j in range(n)]
h = [(0, 0, 0)]
while h:
    cost, x, y = heapq.heappop(h)
    if x == n - 1 and y == m - 1:
        result = cost
        break
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if arr[nx][ny] == "0":
                heapq.heappush(h, (cost, nx, ny))
            else:
                heapq.heappush(h, (cost + 1, nx, ny))

print(result)
