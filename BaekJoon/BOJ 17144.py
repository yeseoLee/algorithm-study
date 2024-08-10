# 골드 4 미세먼지 안녕! https://www.acmicpc.net/problem/17144

import sys
from copy import deepcopy

input = sys.stdin.readline

R, C, T = map(int, input().split())

# -1: 공기청정기, 나머지: 미세먼지 양
arr = []
cleaners = []
for i in range(R):
    line = list(map(int, input().split()))
    for j, val in enumerate(line):
        if val == -1:
            cleaners.append(i)
            line[j] = 0
    arr.append(line)

dx, dy = [0, 0, +1, -1], [+1, -1, 0, 0]


# 미세먼지 확산
def pollute(arr):
    nxt_arr = deepcopy(arr)
    for x in range(R):
        for y in range(C):
            if arr[x][y] < 5:
                continue
            spread_amount = arr[x][y] // 5
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and (ny != 0 or nx not in cleaners):
                    nxt_arr[nx][ny] += spread_amount
                    nxt_arr[x][y] -= spread_amount
    return nxt_arr


# 공기청정기 작동
def clean(arr):
    x1, x2 = cleaners

    # 1
    for x in range(x1 - 1, 0, -1):
        arr[x][0] = arr[x - 1][0]
    arr[0] = arr[0][1:] + [0]
    for x in range(x1):
        arr[x][-1] = arr[x + 1][-1]
    arr[x1] = [0, 0] + arr[x1][1:-1]

    # 2
    for x in range(x2 + 1, R - 1):
        arr[x][0] = arr[x + 1][0]
    arr[-1] = arr[-1][1:] + [0]
    for x in range(R - 2, x2 - 1, -1):
        arr[x + 1][-1] = arr[x][-1]
    arr[x2] = [0, 0] + arr[x2][1:-1]

    return arr


for _ in range(T):
    arr = pollute(arr)
    arr = clean(arr)

print(sum([sum(li) for li in arr]))
