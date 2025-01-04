from collections import deque
import sys


input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def solution(N, M, board):
    # 외부 공기 표시
    def _outer():
        visited = [[False for j in range(M)] for i in range(N)]
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    continue
                if not (i == 0 or i == N - 1 or j == 0 or j == M - 1):
                    continue
                if board[i][j] == 0 or board[i][j] == -1:
                    que = deque([(i, j)])
                    visited[i][j] = True
                    while que:
                        x, y = que.popleft()
                        board[x][y] = -1
                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if not (0 <= nx < N and 0 <= ny < M):
                                continue
                            if visited[nx][ny]:
                                continue
                            if board[nx][ny] == 0 or board[nx][ny] == -1:
                                board[nx][ny] = -1
                                visited[nx][ny] = True
                                que.append((nx, ny))
        if sum([sum(row) for row in board]) == -1 * N * M:
            return True
        return False

    def _cheeze():
        visited = [[False for j in range(M)] for i in range(N)]
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    continue
                if board[i][j] == 1:
                    visited[i][j] = True
                    que = deque([(i, j)])
                    while que:
                        x, y = que.popleft()
                        cnt = 0
                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if not (0 <= nx < N and 0 <= ny < M):
                                continue
                            if visited[nx][ny]:
                                continue
                            if board[nx][ny] == 1:
                                visited[nx][ny] = True
                                que.append((nx, ny))
                            elif board[nx][ny] == -1:
                                cnt += 1
                        if cnt >= 2:
                            board[x][y] = -1

    time = 0
    while True:
        if _outer():
            return time
        _cheeze()
        time += 1


print(solution(N, M, board))
