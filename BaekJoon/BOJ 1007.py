import sys
from math import sqrt
input = sys.stdin.readline


def getDistance(dx, dy):
    return sqrt(dx**2 + dy**2)


def find(idx, cnt):
    global answer

    if idx == n:
        return
    if cnt == n//2:
        dx, dy = 0, 0
        for i in range(n):
            if visited[i]:
                dx += dots[i][0]
                dy += dots[i][1]
            else:
                dx -= dots[i][0]
                dy -= dots[i][1]
        answer = min(answer, getDistance(dx, dy))
        return

    find(idx+1, cnt)
    visited[idx] = True
    find(idx+1, cnt+1)
    visited[idx] = False


T = int(input())
for _ in range(T):
    answer = 1e9
    n = int(input())
    dots = [list(map(int, input().split())) for i in range(n)]
    visited = [False]*n
    find(0, 0)
    print(answer)
''' TIME LIMIT
import sys
import math
import heapq
input = sys.stdin.readline


def getVector(dot1, dot2):
    dx = dot1[0] - dot2[0]
    dy = dot1[1] - dot2[1]
    return (dx, dy)


def getDistance(dx, dy):
    return math.sqrt(dx**2 + dy**2)


def find(i_start, j_start, dx, dy, cnt):
    if cnt == n//2:
        answer.append(getDistance(dx, dy))
        return
    for i in range(i_start, n):
        for j in range(j_start, n):
            if graph[i][j] != 0 and not visited[i] and not visited[j]:
                visited[i], visited[j] = 1, 1
                find(i, j, dx + graph[i][j][0], dy + graph[i][j][1], cnt+1)
                visited[i], visited[j] = 0, 0
        j_start = 0


T = int(input())
for _ in range(T):
    n = int(input())
    dots = [list(map(int, input().split())) for i in range(n)]
    graph = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dx, dy = getVector(dots[i], dots[j])
            graph[i][j] = (dx, dy)
            graph[j][i] = (-dx, -dy)
    visited = [0]*n
    answer = []
    find(0, 0, 0, 0, 0)
    print(min(answer))
'''
