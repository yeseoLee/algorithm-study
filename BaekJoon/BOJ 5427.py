# BOJ 5427 골드 4 https://www.acmicpc.net/problem/5427

import sys
from collections import deque

input = sys.stdin.readline

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]


def exit(w, h, building):
    visited = [[False for i in range(w)] for i in range(h)]
    que = deque()
    fires = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == "@":
                que.append((i, j))
                building[i][j] = "."
                visited[i][j] = True
            elif building[i][j] == "*":
                fires.append((i, j))

    t = 0
    while que:
        t += 1
        # fire
        new_fires = []
        for i, j in fires:
            for a in range(4):
                ni, nj = i + di[a], j + dj[a]
                if 0 <= ni < h and 0 <= nj < w:
                    if building[ni][nj] == ".":
                        building[ni][nj] = "*"
                        new_fires.append((ni, nj))
        fires = new_fires

        # person
        nxt_que = deque()
        for i, j in que:
            for a in range(4):
                ni, nj = i + di[a], j + dj[a]
                if 0 <= ni < h and 0 <= nj < w:
                    if building[ni][nj] == "." and not visited[ni][nj]:
                        visited[ni][nj] = True
                        nxt_que.append((ni, nj))
                else:
                    return t
        que = nxt_que

    return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(h)]
    print(exit(w, h, building))
