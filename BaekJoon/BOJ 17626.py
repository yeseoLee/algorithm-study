import math

n = int(input())


def solution(n):
    one, two, three = [], [], []

    # 1
    k = int(math.sqrt(n))
    if k**2 == n:
        return 1
    for i in range(1, k + 1):
        one.append(i**2)

    # 2
    for i in range(len(one)):
        for j in range(i, len(one)):
            if one[i] + one[j] > n:
                break
            elif one[i] + one[j] < n:
                two.append(one[i] + one[j])
            else:
                return 2

    # 3
    for i in two:
        for j in one:
            if i + j > n:
                break
            elif i + j < n:
                three.append(i + j)
            else:
                return 3

    # 4
    for i in three:
        for j in one:
            if i + j > n:
                break
            else:
                return 4


print(solution(n))
