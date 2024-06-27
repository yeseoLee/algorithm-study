# BOJ 9613 실버 4 GCD 합

import sys

input = sys.stdin.readline


def get_sum_gcd(arr: list):
    sum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                gcd = get_gcd(arr[i], arr[j])
            else:
                gcd = get_gcd(arr[j], arr[i])
            sum += gcd
    return sum


def get_gcd(x: int, y: int):
    if y == 0:
        return x
    else:
        return get_gcd(y, x % y)


t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(get_sum_gcd(arr[1:]))
