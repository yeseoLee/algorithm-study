# 백준 플레티넘 5 히스토그램에서 가장 큰 직사각형 https://www.acmicpc.net/problem/6549

import sys

input = sys.stdin.readline


def solution(arr):
    answer = 0
    stack = []
    for now_i, now_v in enumerate(arr):
        prev_i = now_i
        while stack and stack[-1][1] >= now_v:
            prev_i, prev_v = stack.pop()
            answer = max(answer, (now_i - prev_i) * prev_v)
        stack.append((prev_i, now_v))

    while stack:
        i, v = stack.pop()
        answer = max(answer, (len(arr) - i) * v)
    return answer


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    print(solution(arr[1:]))
