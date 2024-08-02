# 골드 5 뱀과 사다리 게임 https://www.acmicpc.net/problem/16928

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [0] * 101
visited = [False] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

answer = 100

visited[1] = True
que = deque([(0, 1)])
while que:
    cnt, now = que.popleft()
    if now == 100:
        answer = cnt
        break

    max_nxt = now
    for dice in range(1, 7):
        nxt = now + dice
        if nxt > 100 or visited[nxt]:
            continue
        if board[nxt] == 0:
            # 사다리나 뱀이 아니면서 가장 멀리가는 경우
            max_nxt = nxt
        else:
            visited[nxt] = True
            que.append((cnt + 1, board[nxt]))

    if max_nxt != now:
        visited[max_nxt] = True
        que.append((cnt + 1, max_nxt))

print(answer)
