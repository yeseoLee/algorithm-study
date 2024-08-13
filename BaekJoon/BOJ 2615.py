# 실버 1 오목 https://www.acmicpc.net/problem/2615

import sys

BOARD_SIZE = 19
FIVE = 5

board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]

di, dj = [1, 0, 1, -1], [0, 1, 1, 1]


def is_five(i, j, d):
    # 육목 1
    ni, nj = i - di[d], j - dj[d]
    if 0 <= ni < BOARD_SIZE and 0 <= nj < BOARD_SIZE:
        if board[i][j] == board[ni][nj]:
            return 0

    for _ in range(FIVE):
        ni += di[d]
        nj += dj[d]
        if not (0 <= ni < BOARD_SIZE and 0 <= nj < BOARD_SIZE):
            return 0
        if board[i][j] != board[ni][nj]:
            return 0

    # 육목 2
    ni += di[d]
    nj += dj[d]
    if 0 <= ni < BOARD_SIZE and 0 <= nj < BOARD_SIZE:
        if board[i][j] == board[ni][nj]:
            return 0

    return board[i][j]


for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] != 0:
            for d in range(4):
                result = is_five(i, j, d)
                if result != 0:
                    print(result)
                    print(i + 1, j + 1)
                    sys.exit(0)
print(0)
