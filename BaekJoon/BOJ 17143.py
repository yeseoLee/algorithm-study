import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

board = [[-1 for col in range(C)] for row in range(R)]
sharks = [None] * M
for i in range(M):
    # r,c: 위치 / s: 속력, d: 이동방향, z: 크기
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = i
    sharks[i] = [r - 1, c - 1, s, d - 1, z]


dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]


def change_d(d):
    if d == 0 or d == 2:
        return d + 1
    else:
        return d - 1


catched = 0
for c in range(C):
    # catch
    for r in range(R):
        if board[r][c] != -1:
            idx = board[r][c]
            catched += sharks[idx][4]
            sharks[idx] = None
            board[r][c] = -1
            break

    # move
    for i in range(M):
        if sharks[i] is not None:
            # find next
            r, c, s, d, z = sharks[i]
            board[r][c] = -1
            while True:
                r += dr[d] * s
                c += dc[d] * s

                if r < 0:
                    s = -r
                    r = 0
                elif r > R - 1:
                    s = r - (R - 1)
                    r = R - 1
                elif c < 0:
                    s = -c
                    c = 0
                elif c > C - 1:
                    s = c - (C - 1)
                    c = C - 1
                else:
                    break

                d = change_d(d)

            # update sharks
            sharks[i][0] = r
            sharks[i][1] = c
            sharks[i][3] = d

    # update board
    for i in range(M):
        if sharks[i] is not None:
            # eat
            r, c, s, d, z = sharks[i]
            if board[r][c] != -1:
                other_idx = board[r][c]
                if sharks[other_idx][4] > sharks[i][4]:
                    sharks[i] = None
                else:
                    sharks[other_idx] = None

            if sharks[i] is not None:
                board[r][c] = i

print(catched)
