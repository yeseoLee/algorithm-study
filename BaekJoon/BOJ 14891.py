# 골드 5 톱니바퀴 https://www.acmicpc.net/problem/14891

import sys
from collections import deque

input = sys.stdin.readline

GEAR_NUM = 4

# 4*8, 0: N극, 1: S극
gears = [deque(list(map(int, list(input().rstrip())))) for _ in range(GEAR_NUM)]
k = int(input())
# 바퀴번호, 방향(1: 시계, -1: 반시계)
rotates = [list(map(int, input().split())) for _ in range(k)]


def get_score():
    return sum(gears[i][0] * (2**i) for i in range(GEAR_NUM))


def left(num, dir):
    if num < 0 or gears[num][2] == gears[num + 1][-2]:
        return
    left(num - 1, -dir)
    gears[num].rotate(dir)


def right(num, dir):
    if num > 3 or gears[num][-2] == gears[num - 1][2]:
        return
    right(num + 1, -dir)
    gears[num].rotate(dir)


# 회전하기 전 인접한 기어와 마주보는 극이 다르면 회전할 때 같이 회전(방향은 반대로)
for num, dir in rotates:
    left(num - 2, -dir)
    right(num, -dir)
    gears[num - 1].rotate(dir)

print(get_score())
