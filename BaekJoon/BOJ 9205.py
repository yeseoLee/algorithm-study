# 골드 5 맥주 마시면서 걸어가기 https://www.acmicpc.net/problem/9205

import sys

input = sys.stdin.readline

MAX_BEERS = 20
BEER_DISTANCE = 50


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def is_happy(p1, p2):
    return get_distance(p1, p2) <= MAX_BEERS * BEER_DISTANCE


def solution(s, graphs, e):
    visited = [False] * N
    stack = [s]
    while stack:
        now = stack.pop()
        if is_happy(now, e):
            return "happy"
        for i, v in enumerate(graphs):
            if not visited[i] and is_happy(now, v):
                visited[i] = True
                stack.append(v)
    return "sad"


T = int(input())
for _ in range(T):
    N = int(input())
    house = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for i in range(N)]
    rock = list(map(int, input().split()))

    print(solution(house, stores, rock))
