from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]


def get_start_point():
    for i in range(N):
        for j in range(M):
            if board[i][j] == "I":
                board[i][j] = "O"
                return (i, j)


def meet(x, y):
    answer = 0
    dx, dy = [+1, -1, 0, 0], [0, 0, +1, -1]
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if board[nx][ny] == "X":
                continue
            if board[nx][ny] == "P":
                answer += 1
            board[nx][ny] = "X"
            que.append((nx, ny))
    return answer if answer != 0 else "TT"


x, y = get_start_point()
answer = meet(x, y)
print(answer)
