from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip().split()) for _ in range(n)]


def solution(n, m, board):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    def _get_target():
        for x in range(n):
            for y in range(m):
                if board[x][y] == "2":
                    return x, y

    def _bfs(x, y, c):
        board[x][y] = c
        que = deque([(x, y, c)])
        while que:
            x, y, c = que.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "1":
                    board[nx][ny] = c + 1
                    que.append((nx, ny, c + 1))

    def _not_arrived():
        for x in range(n):
            for y in range(m):
                if board[x][y] == "1":
                    board[x][y] = -1
                elif board[x][y] == "0":
                    board[x][y] = 0

    sx, sy = _get_target()
    _bfs(sx, sy, 0)
    _not_arrived()

    for x in range(n):
        print(*board[x])
    return


solution(n, m, board)
