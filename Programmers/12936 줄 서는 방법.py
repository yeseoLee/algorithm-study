import math


def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []

    while arr:
        # k 번째: 인덱스 값으로 변환(k - 1)
        a = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(a))

        k %= math.factorial(n - 1)
        n -= 1

    return answer
