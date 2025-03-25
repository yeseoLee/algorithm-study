import sys


input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


def solution(a1, a0, c, n0):
    #  a1 * n + a0 ≤ c × n
    if a1 > c:
        return 0
    return int((c - a1) * n0 >= a0)


print(solution(a1, a0, c, n0))
