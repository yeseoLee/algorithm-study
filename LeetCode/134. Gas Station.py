from typing import List
from collections import deque


# 28ms / 23.28MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start


class SolutionFailed:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        tank = [0] * l
        for i in range(l):
            tank[i] = (gas[i] - cost[(i + 1) % l], i)

        if sum([x[0] for x in tank]) < 0:
            return -1

        print(tank)
        que = deque(tank)
        cnt, now = 0, 0
        while cnt < 5:
            x, i = que.popleft()
            que.append((x, i))
            now += x
            if now < 0:
                cnt, now = 0, 0
            else:
                cnt += 1

        return que[0][1] + 1
