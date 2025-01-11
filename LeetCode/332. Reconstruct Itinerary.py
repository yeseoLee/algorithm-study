from collections import defaultdict
from typing import List


# 재귀
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)

        route = []

        def _dfs(cur_v):
            while graph[cur_v]:
                _dfs(graph[cur_v].pop())
            route.append(cur_v)

        _dfs("JFK")
        return route[::-1]


# 재귀를 반복으로
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # define graph by defaultdict
        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]
