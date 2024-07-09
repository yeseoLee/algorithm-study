def solution(m, n, puddles):
    # init
    board = [[0 for i in range(m + 1)] for j in range(n + 1)]
    board[1][1] = 1

    # dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue

            # from left & up
            left, up = 0, 0
            if [j - 1, i] not in puddles:
                left = board[i][j - 1]
            if [j, i - 1] not in puddles:
                up = board[i - 1][j]

            board[i][j] += (left + up) % 1000000007

    for i in range(n + 1):
        print(board[i])
    return board[n][m]
