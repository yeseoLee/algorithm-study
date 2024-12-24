import sys

input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def get_color(x, y, k):
    blue = False
    white = False
    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[i][j] == 1:
                blue = True
            else:
                white = True
            if blue and white:
                return -1
    if blue:
        return 1
    else:
        return 0


white, blue = 0, 0


def count_papers(x, y, k):
    global white, blue
    if get_color(x, y, k) == 0:
        white += 1
    elif get_color(x, y, k) == 1:
        blue += 1
    else:
        count_papers(x, y, k // 2)
        count_papers(x, y + k // 2, k // 2)
        count_papers(x + k // 2, y, k // 2)
        count_papers(x + k // 2, y + k // 2, k // 2)


count_papers(0, 0, n)
print(white)
print(blue)
