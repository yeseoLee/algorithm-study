#BOJ 17142
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
org_board = []
virus_list = []
min_time = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    org_board.append(data)
    for j in range(n):
        if data[j] == 2:
            org_board[i][j] = -1
            virus_list.append((i, j))


def check(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return False
    return True


def combination(virus_list, num):
    result = []
    if num > len(virus_list):
        return result
    if num == 1:
        for l in virus_list:
            result.append([l])
    elif num > 1:
        for i in range(len(virus_list)-num+1):
            for temp in combination(virus_list[i+1:], num-1):
                result.append(temp+[virus_list[i]])
    return result


def bfs(board, case):
    global min_time
    visited = [[False]*n for _ in range(n)]
    q = deque()
    if check(board):
        min_time = min(min_time, 0)
        return

    for virus in case:
        x, y = virus
        visited[x][y] = True
        board[x][y] = -2
        q.append((x, y, 0))
    end_time = 0
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    continue
                else:
                    if board[nx][ny] == 0:
                        end_time = max(end_time, time + 1)
                    board[nx][ny] = -2
                    visited[nx][ny] = True
                    q.append((nx, ny, time+1))

    if check(board):
        min_time = min(min_time, end_time)


for case in combination(virus_list, m):
    board = [item[:] for item in org_board]
    bfs(board, case)

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)
