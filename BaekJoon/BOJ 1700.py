import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

priority = [deque() for _ in range(K + 1)]
for i, v in enumerate(arr):
    priority[v].append(i)

using = [False] * (K + 1)


def get_lowest_priority():
    e, lowest_priority = 0, 0
    for i in range(1, K + 1):
        if not using[i]:
            continue
        if not priority[i]:
            e = i
            break
        if priority[i][0] > lowest_priority:
            e = i
            lowest_priority = priority[i][0]
    return e


unplug_cnt = 0
for i in arr:
    if sum(using) >= N and not using[i]:
        unplug_cnt += 1
        lp = get_lowest_priority()
        using[lp] = False

    using[i] = True
    priority[i].popleft()

print(unplug_cnt)
